# Generated by Django 4.0.5 on 2022-11-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_category_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='starting_bid',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='bids',
        ),
    ]