# Generated by Django 3.2 on 2022-02-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0060_auto_20220217_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('can be a diva', 'CAN BE A DIVA'), ('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('easy to care for', 'EASY TO CARE FOR')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('fast grower', 'FAST GROWER'), ('takes its time', 'TAKES ITS TIME'), ('lifelong friend', 'LIFELONG FRIEND')], max_length=254),
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
            field=models.CharField(blank=True, choices=[('summer', 'SUMMER'), ('valentines', 'VALENTINES'), ('winter', 'WINTER'), ('spring', 'SPRING')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('10kg', '10kg'), ('one size', 'ONE SIZE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep cool', 'KEEP COOL'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep warm', 'KEEP WARM')], max_length=254),
        ),
    ]