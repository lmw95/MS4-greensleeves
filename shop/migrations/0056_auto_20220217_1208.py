# Generated by Django 3.2 on 2022-02-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0055_auto_20220217_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('can be a diva', 'CAN BE A DIVA'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('easy to care for', 'EASY TO CARE FOR'), ('practically unkillable', 'PRACTICALLY UNKILLABLE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('takes its time', 'TAKES ITS TIME'), ('fast grower', 'FAST GROWER'), ('lifelong friend', 'LIFELONG FRIEND')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('prefers humidity', 'PREFERS HUMIDITY'), ('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers dry air', 'PREFERS DRY AIR')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves the shade', 'LOVES THE SHADE'), ('loves a bit of both', 'LOVES A BIT OF BOTH'), ('loves bright light', 'LOVES BRIGHT LIGHT')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('spring', 'SPRING'), ('summer', 'SUMMER'), ('valentines', 'VALENTINES'), ('winter', 'WINTER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('10kg', '10kg'), ('one size', 'ONE SIZE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_need',
            field=models.CharField(blank=True, choices=[('light watering', 'LIGHT WATERING'), ('water only when dry', 'WATER ONLY WHEN DRY'), ('always thirsty', 'ALWAYS THIRSTY')], max_length=254),
        ),
    ]
