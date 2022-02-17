# Generated by Django 3.2 on 2022-02-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_auto_20220217_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('easy to care for', 'EASY TO CARE FOR'), ('can be a diva', 'CAN BE A DIVA')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers humidity', 'PREFERS HUMIDITY'), ('prefers dry air', 'PREFERS DRY AIR')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves a bit of both', 'LOVES A BIT OF BOTH'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('spring', 'SPRING'), ('valentines', 'VALENTINES'), ('summer', 'SUMMER'), ('winter', 'WINTER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('10kg', '10kg'), ('one size', 'ONE SIZE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep cool', 'KEEP COOL'), ('keep warm', 'KEEP WARM'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_need',
            field=models.CharField(blank=True, choices=[('always thirsty', 'ALWAYS THIRSTY'), ('light watering', 'LIGHT WATERING'), ('water only when dry', 'WATER ONLY WHEN DRY')], max_length=254),
        ),
    ]