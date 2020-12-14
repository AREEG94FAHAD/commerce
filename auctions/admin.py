from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, User, Auction_Listings, Comment, Bid

class Auction_ListingsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "bid",  "image", "category_list")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "comment", "time", "items_info")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "new_bid", "items_info")

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(User)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Auction_Listings, Auction_ListingsAdmin )