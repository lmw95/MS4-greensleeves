# Generated by Django 3.2 on 2022-02-15 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='wishlist',
        ),
    ]
