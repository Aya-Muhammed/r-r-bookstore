# Generated by Django 2.1.7 on 2019-02-22 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('classification', models.CharField(choices=[('Art & Design', 'Art & Design'), ('Biographies', 'Biographies'), ('Business', 'Business'), ('Children', 'Children'), ('Cooking & Nutrition', 'Cooking & Nutrition'), ('Crafts & Hobbies', 'Crafts & Hobbies'), ('Egypt', 'Egypt'), ('History & Politics', 'History & Politics'), ('Literature & Fiction', 'Literature & Fiction'), ('Mind & Body', 'Mind & Body'), ('Reference', 'Reference'), ('Religion', 'Religion'), ('Society', 'Society'), ('Sports', 'Sports'), ('Teens', 'Teens'), ('Travel', 'Travel')], default='Art & Design', max_length=2)),
                ('img', models.ImageField(default='', upload_to='books/')),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Book',
            },
        ),
        migrations.CreateModel(
            name='PublishHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('contract', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'PublishHouse',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publish_house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='books.PublishHouse'),
        ),
    ]