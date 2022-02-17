# Generated by Django 3.2 on 2022-02-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0051_auto_20220217_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('can be a diva', 'CAN BE A DIVA'), ('needs a bit of love', 'NEEDS A BIT OF LOVE'), ('easy to care for', 'EASY TO CARE FOR')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('takes its time', 'TAKES ITS TIME'), ('fast grower', 'FAST GROWER'), ('lifelong friend', 'LIFELONG FRIEND')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers dry air', 'PREFERS DRY AIR'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves a bit of both', 'LOVES A BIT OF BOTH'), ('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('winter', 'WINTER'), ('summer', 'SUMMER'), ('spring', 'SPRING'), ('valentines', 'VALENTINES')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('10kg', '10kg'), ('one size', 'ONE SIZE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep cool', 'KEEP COOL'), ('keep warm', 'KEEP WARM')], max_length=254),
        ),
    ]
