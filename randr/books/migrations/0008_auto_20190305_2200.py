# Generated by Django 2.1.7 on 2019-03-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20190305_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=False),
        ),
    ]
