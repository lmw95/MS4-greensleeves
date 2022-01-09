# Generated by Django 3.2 on 2022-01-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20220109_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('easy to care for', 'EASY TO CARE FOR'), ('can be a diva', 'CAN BE A DIVA')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('fast grower', 'FAST GROWER'), ('takes its time', 'TAKES ITS TIME'), ('lifelong friend', 'LIFELONG FRIEND')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('prefers humidity', 'PREFERS HUMIDITY'), ('prefers dry air', 'PREFERS DRY AIR'), ('likes a little moisture', 'LIKES A LITTLE MOISTURE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves a bit of both', 'LOVES A BIT OF BOTH'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('winter', 'WINTER'), ('spring', 'SPRING'), ('valentines', 'VALENTINES'), ('summer', 'SUMMER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('1x pack', '1X PACK'), ('one pair', 'ONE PAIR'), ('5kg', '5KG'), ('small', 'SMALL'), ('large', 'LARGE'), ('10kg', '10KG'), ('one bunch', 'ONE BUNCH'), ('500ml', '500ml'), ('20kg', '20KG'), ('1l', '1L'), ('various sizes', 'VARIOUS SIZES'), ('medium', 'MEDIUM')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep warm', 'KEEP WARM'), ('keep cool', 'KEEP COOL'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='water_need',
            field=models.CharField(blank=True, choices=[('light watering', 'LIGHT WATERING'), ('always thirsty', 'ALWAYS THIRSTY'), ('water only when dry', 'WATER ONLY WHEN DRY')], max_length=254),
        ),
    ]