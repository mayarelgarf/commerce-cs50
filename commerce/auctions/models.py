
from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class auction_comments(models.Model):
    comment = models.TextField(max_length = 300)  

class category(models.Model):
    category_name= models.CharField(max_length = 100)
    def __str__(self) :
        return self.category_name

class starting_bid (models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete= models.CASCADE,blank= True,null=True,related_name='usersbid') 
    def __str__(self) :
        return str(self.bid)


class auction_listing(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    price = models.ForeignKey(starting_bid,on_delete=models.CASCADE,blank=True,null=True, related_name = 'auction_bid' )
    listing_pic = models.CharField(max_length=200,blank= True,null=True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE,blank= True,null=True,related_name='user')
    category= models.ForeignKey(category,max_length= 100,blank=True,null=True, related_name='category',on_delete=models.CASCADE)
    comments = models.ForeignKey(auction_comments,on_delete=models.CASCADE,blank=True,null=True, related_name = 'auction_comments')
    active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User,blank = True, null = True, related_name = 'watchlist')

    def __str__(self):
        return self.title



