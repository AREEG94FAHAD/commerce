# Generated by Django 3.1.3 on 2020-12-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_bid_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listings',
            name='whatchlist',
            field=models.BooleanField(default=False),
        ),
    ]
