# Generated by Django 3.2 on 2022-01-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20220109_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_multiple',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('easy to care for', 'EASY TO CARE FOR'), ('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('can be a diva', 'CAN BE A DIVA')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('lifelong friend', 'LIFELONG FRIEND'), ('takes its time', 'TAKES ITS TIME'), ('fast grower', 'FAST GROWER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers dry air', 'PREFERS DRY AIR'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves a bit of both', 'LOVES A BIT OF BOTH'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('winter', 'WINTER'), ('spring', 'SPRING'), ('summer', 'SUMMER'), ('valentines', 'VALENTINES')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep warm', 'KEEP WARM'), ('keep cool', 'KEEP COOL')], max_length=254),
        ),
    ]
