# Generated by Django 3.1 on 2020-08-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=50)),
                ('product_description', models.CharField(default='', max_length=100)),
                ('product_price', models.IntegerField(default=0)),
                ('pub_date', models.DateField()),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=80)),
                ('image', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
