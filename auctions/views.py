from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from django.contrib import messages
from .models import User, Category, Bid, Comment, Auction_Listings, WhatchList
from functools import wraps
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            request.session["username"] = user.username
            return HttpResponseRedirect(reverse("index"))
        else:
            
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        request.session["username"] = username
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def login_required(f):
    def wrapper(*args, **kwargs):
        if args[0].user.is_authenticated:
            return f(*args, **kwargs)
        return HttpResponseRedirect(reverse("login"))
    return wrapper


@login_required
def index(request):

    acution_list = Auction_Listings.objects.filter(active=True).all()
    getAllCategory = Category.objects.all()

    return render(request, "auctions/index.html", {
        "list": acution_list,
        "categories": getAllCategory
    })


@login_required
def create_list(request):

    if request.method == "POST":
        category_id = int(request.POST["category"])


        Auction_Listings(
            owner=request.session["username"],
            title=request.POST["title"],
            description=request.POST["description"],
            bid=request.POST["bid"],
            image=request.POST["image"],
            whoBayMoreBid=request.session["username"],
            category_list=Category.objects.get(pk=category_id)).save()

        return HttpResponseRedirect(reverse("index"))

    else:
        category = Category.objects.all()

        return render(request, "auctions/create_list.html", {
            "categories": category

        })


@login_required
def auctionID(request, idOfAuction):

    auction_details = Auction_Listings.objects.get(pk=idOfAuction)
    comments = Comment.objects.filter(items_info=idOfAuction).all()
    cancel = False
    # print(auction_details.owner)
    if auction_details.owner==request.session["username"]:
        cancel = True

    return render(request, "auctions/auction_details.html", {
        "auction": auction_details,
        "comments": comments,
        "cancel":cancel
    })


@login_required
def new_comment(request):
    id = request.POST["id"]
    comment = request.POST["comment"]
    date = datetime.datetime.now()
    print(request.session["username"])
    Comment(
        user=request.session["username"],
        comment=comment,
        time=date,
        items_info=Auction_Listings.objects.get(pk=id)).save()
    return HttpResponseRedirect(reverse("auctionID", args=(id,)))


@login_required
def addToWatchlist(request, acutions_id):
    check = WhatchList.objects.filter(Auctions=acutions_id).all()
    print(check)
    if check:

        return HttpResponseRedirect(reverse("index"))

    getAuctionById = Auction_Listings.objects.get(pk=acutions_id)
    WhatchList(
        whoadd=request.session["username"],
        Auctions=getAuctionById
    ).save()
    return HttpResponseRedirect(reverse("index"))


@login_required
def DisplayWhatchList(request):
    getAllWhatchList = WhatchList.objects.filter(
        whoadd=request.session["username"]).all()
    if getAllWhatchList:
        return render(request, "auctions/DisplayWhatchList.html", {
            "whatList": getAllWhatchList
        })

    else:
        return HttpResponseRedirect(reverse("index"))


@login_required
def removeAuctionFromWhatchlist(request, auctionId):
    WhatchList.objects.get(pk=auctionId).delete()

    return HttpResponseRedirect(reverse("DisplayWhatchList"))




@login_required
def getCategoryById(request, categoryId):
    getItems = Auction_Listings.objects.filter(category_list=categoryId).all()

    return render(request, "auctions/index.html", {
        "list": getItems,
        "categories": Category.objects.all()

    })


@login_required
def getbidId(request, bidId):
    newBid = request.POST["newBid"]
    getOldBid = Auction_Listings.objects.filter(pk=bidId).only('bid')
    print(getOldBid[0].bid)
    if getOldBid[0].bid < int(newBid):
        getAuction = Auction_Listings.objects.filter(pk=bidId).update(
            bid=newBid, whoBayMoreBid=request.session["username"])
        return HttpResponseRedirect(reverse("auctionID", args=(bidId,)))
    else:
        messages.error(request, 'Use high bid if you want this items please!.')
        return HttpResponseRedirect(reverse("auctionID", args=(bidId,)))

@login_required
def cancelAuction(request, auctionsId):
    getAuctions = Auction_Listings.objects.filter(pk=auctionsId).update(
        active=False
    )

    getwiner = Auction_Listings.objects.filter(pk=auctionsId).values('whoBayMoreBid')


    messages.success(request, 'congragulation '+ str((getwiner[0]['whoBayMoreBid'])))
    return HttpResponseRedirect(reverse("auctionID", args=(auctionsId,)))