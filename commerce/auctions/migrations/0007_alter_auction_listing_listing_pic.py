# Generated by Django 4.0.5 on 2022-11-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auction_listing_listing_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='listing_pic',
            field=models.URLField(blank=True, null=True),
        ),
    ]