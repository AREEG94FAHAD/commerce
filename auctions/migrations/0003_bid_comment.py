# Generated by Django 3.1.3 on 2020-12-01 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20201130_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('comment', models.TextField()),
                ('time', models.TimeField()),
                ('items_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_comment', to='auctions.auction_listings')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=64)),
                ('new_bid', models.IntegerField()),
                ('items_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_bid', to='auctions.auction_listings')),
            ],
        ),
    ]
