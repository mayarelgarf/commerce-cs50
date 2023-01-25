from django.contrib import admin
from .models import auction_comments, auction_listing,category,User,starting_bid

# Register your models here.
admin.site.register(auction_listing)
admin.site.register(starting_bid)
admin.site.register(auction_comments)
admin.site.register(category)
admin.site.register(User)