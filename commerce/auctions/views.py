
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User,auction_listing,auction_comments,category, starting_bid


def index(request):
    active_listings = auction_listing.objects.filter(active = True)
    return render(request, "auctions/index.html",{"active_listings":active_listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
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
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required        
def create_listing(request):
    if request.method =='GET':
        categories = category.objects.all()
        return render(request,'auctions/create_listing.html',{'categories_dropdown': categories})
    elif request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.POST['image']
        price = request.POST['price']
        listing_category = request.POST['category']
        current_user = request.user
        getting_category = category.objects.get(category_name =listing_category)
        bid = starting_bid(bid = price, user = current_user)
        bid.save()
        created_listing = auction_listing(
            title=title,
            description=description,
            listing_pic= image,
            category = getting_category,
            price = bid,
            owner= current_user
            )

        created_listing.save()

        return HttpResponseRedirect(reverse(index))

def listing_page(request,id):
    listing = auction_listing.objects.get(pk = id)
    listing_category = category.objects.get(category_name=listing.category)
    watchlist =  request.user in listing.watchlist.all()
    owner = request.user.username == listing.owner.username
        
    return render (request,"auctions/listing_page.html",{"listing":listing,'ls_category':listing_category, "watchlist":watchlist,'owner':owner} )


def add_watchlist(request,id):
    if request.method == 'POST':
        entire_listing = auction_listing.objects.get(pk=id)
        current_user= request.user
        entire_listing.watchlist.add(current_user)
        return HttpResponseRedirect(reverse("listing_page",args=(id,)))


def remove_watchlist(request,id):
    if request.method == 'POST':
        entire_listing = auction_listing.objects.get(pk=id)
        current_user= request.user
        entire_listing.watchlist.remove(current_user)
        return HttpResponseRedirect(reverse("listing_page",args=(id,)))


def watchlist(request):
    user = request.user
    user_watchlist = user.watchlist.all() 
    return render(request,'auctions/watchlist.html',{'user_watchlist': user_watchlist} )


def add_bid(request,id):
    if request.method == "POST":
        users_bid = request.POST["bid"]
        auction_bid_id = auction_listing.objects.get(pk=id)
        if int(users_bid) > auction_bid_id.price.bid:
            new_bid = starting_bid(user = request.user, bid = users_bid )
            new_bid.save()
            auction_bid_id.price = new_bid
            auction_bid_id.save()
            return render(request,'auctions/listing_page.html',{'listing':auction_bid_id,'message': 'bid updated successfully'})

        else:
            return render (request,'auctions/listing_page.html',{'listing':auction_bid_id,'message': 'bid update failed'})

def close_auction(request,id):
    if request.method == "POST":
        close_auction = request.POST['close_auction']
        auction = auction_listing.objects.get(pk=id)
        auction.active = False
        auction.save()
        listing_category = category.objects.get(category_name=auction.category)
        watchlist =  request.user in auction.watchlist.all()
        owner = request.user.username == auction.owner.username
        return render (request,"auctions/listing_page.html",{"listing":auction,'ls_category':listing_category, "watchlist":watchlist,'owner':owner, 'message':'your auction is successfully closed!'} )

       


    
    
    
        
   


        
        

        

        

