# Generated by Django 3.1 on 2020-08-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200820_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items_json',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
