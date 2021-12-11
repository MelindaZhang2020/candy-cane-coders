# Generated by Django 3.2.4 on 2021-12-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='item',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='gifts',
            field=models.ManyToManyField(blank=True, related_name='wishlist_gifts', to='gifts.Gift'),
        ),
    ]
