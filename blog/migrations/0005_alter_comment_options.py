# Generated by Django 3.2 on 2022-02-17 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_added']},
        ),
    ]
