# Generated by Django 3.2 on 2022-02-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0046_auto_20220217_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('can be a diva', 'CAN BE A DIVA'), ('easy to care for', 'EASY TO CARE FOR'), ('needs a bit of love', 'NEEDS A BIT OF LOVE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('lifelong friend', 'LIFELONG FRIEND'), ('fast grower', 'FAST GROWER'), ('takes its time', 'TAKES ITS TIME')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers dry air', 'PREFERS DRY AIR'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves the shade', 'LOVES THE SHADE'), ('loves a bit of both', 'LOVES A BIT OF BOTH')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('summer', 'SUMMER'), ('valentines', 'VALENTINES'), ('spring', 'SPRING'), ('winter', 'WINTER')], max_length=254),
        ),
    ]