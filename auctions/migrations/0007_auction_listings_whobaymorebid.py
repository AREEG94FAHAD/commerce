# Generated by Django 3.1.3 on 2020-12-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20201203_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listings',
            name='whoBayMoreBid',
            field=models.CharField(default=models.CharField(max_length=64), max_length=64),
        ),
    ]
