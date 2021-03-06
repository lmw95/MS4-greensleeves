# Generated by Django 3.2 on 2022-01-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20220112_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sale_price',
            new_name='sale_discount',
        ),
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
            field=models.CharField(blank=True, choices=[('loves a bit of both', 'LOVES A BIT OF BOTH'), ('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('winter', 'WINTER'), ('valentines', 'VALENTINES'), ('spring', 'SPRING'), ('summer', 'SUMMER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('10kg', '10kg'), ('one size', 'ONE SIZE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep warm', 'KEEP WARM'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep cool', 'KEEP COOL')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_need',
            field=models.CharField(blank=True, choices=[('light watering', 'LIGHT WATERING'), ('water only when dry', 'WATER ONLY WHEN DRY'), ('always thirsty', 'ALWAYS THIRSTY')], max_length=254),
        ),
    ]
