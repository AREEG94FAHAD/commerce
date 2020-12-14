from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_list", views.create_list, name="create_list"),
    path("<int:idOfAuction>", views.auctionID, name="auctionID"),
    path("new_comment", views.new_comment, name="new_comment"),
    path("addToWatchlist/<int:acutions_id>", views.addToWatchlist, name="addToWatchlist"),
    path("DisplayWhatchList", views.DisplayWhatchList, name="DisplayWhatchList"),
    path("removeAuctionFromWhatchlist/<int:auctionId>", views.removeAuctionFromWhatchlist, name="removeAuctionFromWhatchlist"),
    # path("category", views.getAllCategory, name="category"),
    path("getCategoryById/<int:categoryId>", views.getCategoryById, name="getCategoryById"),
    path("getbidId/<int:bidId>", views.getbidId, name="Bid"),
    path("cancelAuction/<int:auctionsId>", views.cancelAuction,name="cancelAuction")
]
