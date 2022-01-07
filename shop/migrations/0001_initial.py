# Generated by Django 3.2 on 2022-01-07 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('is_plant', models.BooleanField(default=False, null=True)),
                ('is_accessory', models.BooleanField(default=False, null=True)),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(default=models.CharField(max_length=254), max_length=254)),
                ('height', models.CharField(blank=True, max_length=254, null=True)),
                ('has_size_choice', models.BooleanField(default=False, null=True)),
                ('size', models.CharField(blank=True, choices=[('large', 'LARGE'), ('5kg', '5KG'), ('small', 'SMALL'), ('10kg', '10KG'), ('medium', 'MEDIUM'), ('various sizes', 'VARIOUS SIZES'), ('1l', '1L'), ('500ml', '500ml'), ('20kg', '20KG')], max_length=254)),
                ('has_weight_choice', models.BooleanField(default=False, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_multiple', models.BooleanField(default=False, null=True)),
                ('water_need', models.CharField(blank=True, choices=[('always thirsty', 'ALWAYS THIRSTY'), ('water only when dry', 'WATER ONLY WHEN DRY'), ('light watering', 'LIGHT WATERING')], max_length=254)),
                ('humidity_need', models.CharField(blank=True, choices=[('likes a little moisture', 'LIKES A LITTLE MOISTURE'), ('prefers dry air', 'PREFERS DRY AIR'), ('prefers humidity', 'PREFERS HUMIDITY')], max_length=254)),
                ('growth_need', models.CharField(blank=True, choices=[('fast grower', 'FAST GROWER'), ('lifelong friend', 'LIFELONG FRIEND'), ('takes its time', 'TAKES ITS TIME')], max_length=254)),
                ('temp_need', models.CharField(blank=True, choices=[('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'), ('keep warm', 'KEEP WARM'), ('keep cool', 'KEEP COOL')], max_length=254)),
                ('light_need', models.CharField(blank=True, choices=[('loves bright light', 'LOVES BRIGHT LIGHT'), ('needs a bit of both', 'LOVES A BIT OF BOTH'), ('loves the shade', 'LOVES THE SHADE')], max_length=254)),
                ('ease_of_care', models.CharField(blank=True, choices=[('easy to care for', 'EASY TO CARE FOR'), ('practically unkillable', 'PRACTICALLY UNKILLABLE'), ('can be a diva', 'CAN BE A DIVA'), ('needs a bit of love', 'NEEDS A BIT OF LOVE')], max_length=254)),
                ('is_in_seasonal_collection', models.BooleanField(blank=True, default=False, null=True)),
                ('seasonal_collection', models.CharField(blank=True, choices=[('valentines', 'VALENTINES'), ('spring', 'SPRING'), ('summer', 'SUMMER'), ('winter', 'WINTER')], max_length=254)),
                ('top_tip', models.TextField(blank=True, null=True)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('is_on_sale', models.BooleanField(blank=True, default=False, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1054, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category')),
            ],
        ),
    ]
