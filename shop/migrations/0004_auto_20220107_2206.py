# Generated by Django 3.2 on 2022-01-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220107_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('easy to care for', 'EASY TO CARE FOR'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('can be a diva', 'CAN BE A DIVA')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('fast grower', 'FAST GROWER'), ('lifelong friend', 'LIFELONG FRIEND'), ('takes its time', 'TAKES ITS TIME')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers dry air', 'PREFERS DRY AIR'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves bright light', 'LOVES BRIGHT LIGHT'), ('needs a bit of both', 'LOVES A BIT OF BOTH'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('summer', 'SUMMER'), ('winter', 'WINTER'), ('valentines', 'VALENTINES'), ('spring', 'SPRING')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('20kg', '20KG'), ('5kg', '5KG'), ('large', 'LARGE'), ('small', 'SMALL'), ('1l', '1L'), ('medium', 'MEDIUM'), ('various sizes', 'VARIOUS SIZES'), ('10kg', '10KG'), ('1x pack', '1X PACK'), ('500ml', '500ml')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep warm', 'KEEP WARM'), ('keep cool', 'KEEP COOL')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_need',
            field=models.CharField(blank=True, choices=[('water only when dry', 'WATER ONLY WHEN DRY'), ('always thirsty', 'ALWAYS THIRSTY'), ('light watering', 'LIGHT WATERING')], max_length=254),
        ),
    ]