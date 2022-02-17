# Generated by Django 3.2 on 2022-02-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20220214_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('easy to care for', 'EASY TO CARE FOR'), ('can be a diva', 'CAN BE A DIVA')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('takes its time', 'TAKES ITS TIME'), ('lifelong friend', 'LIFELONG FRIEND'), ('fast grower', 'FAST GROWER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('prefers humidity', 'PREFERS HUMIDITY'), ('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers dry air', 'PREFERS DRY AIR')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves the shade', 'LOVES THE SHADE'), ('loves a bit of both', 'LOVES A BIT OF BOTH')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('spring', 'SPRING'), ('winter', 'WINTER'), ('summer', 'SUMMER'), ('valentines', 'VALENTINES')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep warm', 'KEEP WARM'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep cool', 'KEEP COOL')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_need',
            field=models.CharField(blank=True, choices=[('always thirsty', 'ALWAYS THIRSTY'), ('water only when dry', 'WATER ONLY WHEN DRY'), ('light watering', 'LIGHT WATERING')], max_length=254),
        ),
    ]