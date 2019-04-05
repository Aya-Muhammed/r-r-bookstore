# Generated by Django 2.1.7 on 2019-03-08 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(default=datetime.time)),
                ('location', models.CharField(max_length=25)),
                ('about', models.TextField()),
                ('img', models.ImageField(upload_to='', verbose_name=models.ImageField(default='events/no.png', upload_to='events/'))),
                ('img_inside', models.ImageField(upload_to='', verbose_name=models.ImageField(default='events/no_inside.png', upload_to='events/'))),
            ],
        ),
    ]