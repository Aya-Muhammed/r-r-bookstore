# Generated by Django 2.1.7 on 2019-02-24 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190224_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img_inside',
            field=models.ImageField(default='books/no_inside.png', upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(default='books/no.png', upload_to='books/'),
        ),
    ]