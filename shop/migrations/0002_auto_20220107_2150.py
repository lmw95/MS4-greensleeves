# Generated by Django 3.2 on 2022-01-07 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('easy to care for', 'EASY TO CARE FOR'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('can be a diva', 'CAN BE A DIVA')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('lifelong friend', 'LIFELONG FRIEND'), ('fast grower', 'FAST GROWER'), ('takes its time', 'TAKES ITS TIME')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('prefers dry air', 'PREFERS DRY AIR'), ('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves the shade', 'LOVES THE SHADE'), ('loves bright light', 'LOVES BRIGHT LIGHT'), ('needs a bit of both', 'LOVES A BIT OF BOTH')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('spring', 'SPRING'), ('valentines', 'VALENTINES'), ('summer', 'SUMMER'), ('winter', 'WINTER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('500ml', '500ml'), ('5kg', '5KG'), ('small', 'SMALL'), ('20kg', '20KG'), ('1l', '1L'), ('10kg', '10KG'), ('various sizes', 'VARIOUS SIZES'), ('large', 'LARGE'), ('medium', 'MEDIUM')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep cool', 'KEEP COOL'), ('keep warm', 'KEEP WARM'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE')], max_length=254),
        ),
    ]