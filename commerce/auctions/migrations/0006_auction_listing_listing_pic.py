# Generated by Django 4.0.5 on 2022-11-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_auction_listing_starting_bid_delete_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='listing_pic',
            field=models.URLField(blank=True),
        ),
    ]
