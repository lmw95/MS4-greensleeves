# Generated by Django 3.2 on 2022-02-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_auto_20220217_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('can be a diva', 'CAN BE A DIVA'), ('easy to care for', 'EASY TO CARE FOR'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('practically unkillable', 'PRACTICALLY UNKILLABLE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('fast grower', 'FAST GROWER'), ('takes its time', 'TAKES ITS TIME'), ('lifelong friend', 'LIFELONG FRIEND')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('prefers dry air', 'PREFERS DRY AIR'), ('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('summer', 'SUMMER'), ('valentines', 'VALENTINES'), ('winter', 'WINTER'), ('spring', 'SPRING')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep cool', 'KEEP COOL'), ('keep warm', 'KEEP WARM'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_need',
            field=models.CharField(blank=True, choices=[('light watering', 'LIGHT WATERING'), ('always thirsty', 'ALWAYS THIRSTY'), ('water only when dry', 'WATER ONLY WHEN DRY')], max_length=254),
        ),
    ]