# Generated by Django 3.2 on 2022-02-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_auto_20220217_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('easy to care for', 'EASY TO CARE FOR'), ('can be a diva', 'CAN BE A DIVA'), ('practically unkillable', 'PRACTICALLY UNKILLABLE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('takes its time', 'TAKES ITS TIME'), ('lifelong friend', 'LIFELONG FRIEND'), ('fast grower', 'FAST GROWER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves a bit of both', 'LOVES A BIT OF BOTH'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('valentines', 'VALENTINES'), ('winter', 'WINTER'), ('summer', 'SUMMER'), ('spring', 'SPRING')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep cool', 'KEEP COOL'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep warm', 'KEEP WARM')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_need',
            field=models.CharField(blank=True, choices=[('water only when dry', 'WATER ONLY WHEN DRY'), ('always thirsty', 'ALWAYS THIRSTY'), ('light watering', 'LIGHT WATERING')], max_length=254),
        ),
    ]