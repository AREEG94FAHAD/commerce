from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

class Auction_Listings(models.Model):
    owner =  models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    bid = models.IntegerField()
    image = models.CharField(max_length=250, default='SOME STRING')
    whoBayMoreBid =  models.CharField(max_length=64, default="")
    category_list = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="type")
    active = models.BooleanField(default=True)


class Comment(models.Model):
    user = models.CharField(max_length=64)
    comment = models.TextField()
    time = models.TimeField()
    items_info = models.ForeignKey(Auction_Listings,on_delete=models.CASCADE,related_name="item_comment")

    

class Bid(models.Model):
    client = models.CharField(max_length=64)
    new_bid = models.IntegerField()
    items_info = models.ForeignKey(Auction_Listings,on_delete=models.CASCADE,related_name="item_bid")

class WhatchList(models.Model):
    whoadd = models.CharField(max_length=64)
    Auctions = models.ForeignKey(Auction_Listings, on_delete=models.CASCADE)