# Generated by Django 2.1.7 on 2019-03-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='img_inside1',
            field=models.ImageField(blank=True, default='accessories/no.png', upload_to='accessories/'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='img_inside2',
            field=models.ImageField(blank=True, default='accessories/no.png', upload_to='accessories/'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='img_inside3',
            field=models.ImageField(blank=True, default='accessories/no.png', upload_to='accessories/'),
        ),
        migrations.AlterModelTable(
            name='accessory',
            table='Accessory',
        ),
    ]