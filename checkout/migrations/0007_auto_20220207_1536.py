# Generated by Django 3.2 on 2022-02-07 15:36

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
