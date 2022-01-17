# Generated by Django 3.2 on 2022-01-16 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20220116_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sale_discount',
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ease_of_care',
            field=models.CharField(blank=True, choices=[('can be a diva', 'CAN BE A DIVA'), ('easy to care for', 'EASY TO CARE FOR'), ('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('needs a bit of love', 'NEEDS A BIT OF LOVE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='growth_need',
            field=models.CharField(blank=True, choices=[('takes its time', 'TAKES ITS TIME'), ('fast grower', 'FAST GROWER'), ('lifelong friend', 'LIFELONG FRIEND')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='humidity_need',
            field=models.CharField(blank=True, choices=[('prefers dry air', 'PREFERS DRY AIR'), ('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='light_need',
            field=models.CharField(blank=True, choices=[('loves a bit of both', 'LOVES A BIT OF BOTH'), ('loves bright light', 'LOVES BRIGHT LIGHT'), ('loves the shade', 'LOVES THE SHADE')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_collection',
            field=models.CharField(blank=True, choices=[('winter', 'WINTER'), ('valentines', 'VALENTINES'), ('summer', 'SUMMER'), ('spring', 'SPRING')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('one size', 'ONE SIZE'), ('10kg', '10kg')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='temp_need',
            field=models.CharField(blank=True, choices=[('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep warm', 'KEEP WARM'), ('keep cool', 'KEEP COOL')], max_length=254),
        ),
    ]
