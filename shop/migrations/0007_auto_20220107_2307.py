# Generated by Django 3.2 on 2022-01-07 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20220107_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('can be a diva', 'CAN BE A DIVA'), ('easy to care for', 'EASY TO CARE FOR')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('lifelong friend', 'LIFELONG FRIEND'), ('takes its time', 'TAKES ITS TIME'), ('fast grower', 'FAST GROWER')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves the shade', 'LOVES THE SHADE'), ('needs a bit of both', 'LOVES A BIT OF BOTH'), ('loves bright light', 'LOVES BRIGHT LIGHT')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('winter', 'WINTER'), ('summer', 'SUMMER'), ('spring', 'SPRING'), ('valentines', 'VALENTINES')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('1l', '1L'), ('10kg', '10KG'), ('various sizes', 'VARIOUS SIZES'), ('small', 'SMALL'), ('1x pack', '1X PACK'), ('5kg', '5KG'), ('large', 'LARGE'), ('500ml', '500ml'), ('20kg', '20KG'), ('one pair', 'ONE PAIR'), ('one bunch', 'ONE BUNCH'), ('medium', 'MEDIUM')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep warm', 'KEEP WARM'), ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep cool', 'KEEP COOL')], max_length=254),
        ),
    ]
