# Generated by Django 2.1.7 on 2019-03-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('img', models.ImageField(default='stores/no.png', upload_to='stores/')),
            ],
        ),
    ]