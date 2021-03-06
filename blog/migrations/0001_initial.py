# Generated by Django 3.1 on 2020-08-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('blogPost_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=1111)),
                ('heading1', models.CharField(default='', max_length=1111)),
                ('content1', models.CharField(default='', max_length=10000)),
                ('heading2', models.CharField(default='', max_length=1111)),
                ('content2', models.CharField(default='', max_length=10000)),
                ('heading3', models.CharField(default='', max_length=1111)),
                ('content3', models.CharField(default='', max_length=10000)),
                ('heading4', models.CharField(default='', max_length=1111)),
                ('content4', models.CharField(default='', max_length=10000)),
                ('summary', models.CharField(default='', max_length=10000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
                ('image1', models.ImageField(default='', upload_to='blog/images')),
                ('image2', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
