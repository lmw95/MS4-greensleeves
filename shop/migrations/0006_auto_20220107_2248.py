# Generated by Django 3.2 on 2022-01-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20220107_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('easy to care for', 'EASY TO CARE FOR'), ('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('can be a diva', 'CAN BE A DIVA')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('lifelong friend', 'LIFELONG FRIEND'), ('fast grower', 'FAST GROWER'), ('takes its time', 'TAKES ITS TIME')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers dry air', 'PREFERS DRY AIR'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('needs a bit of both', 'LOVES A BIT OF BOTH'), ('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('summer', 'SUMMER'), ('winter', 'WINTER'), ('spring', 'SPRING'), ('valentines', 'VALENTINES')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('5kg', '5KG'), ('one bunch', 'ONE BUNCH'), ('one pair', 'ONE PAIR'), ('various sizes', 'VARIOUS SIZES'), ('500ml', '500ml'), ('medium', 'MEDIUM'), ('1l', '1L'), ('small', 'SMALL'), ('large', 'LARGE'), ('10kg', '10KG'), ('1x pack', '1X PACK'), ('20kg', '20KG')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep cool', 'KEEP COOL'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep warm', 'KEEP WARM')], max_length=254),
        ),
    ]