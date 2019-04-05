from django.db import models
from datetime import datetime


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class PublishHouse(models.Model):
    name = models.CharField(max_length=25, unique=True)
    location = models.CharField(max_length=50, blank=True)
    contract = models.IntegerField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'PublishHouse'


class Book(models.Model):
    publish_house = models.ForeignKey(PublishHouse, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    objects = models.Manager()

    Art_Design = 'Art & Design'
    Biographies = 'Biographies'
    Business = 'Business'
    Children = 'Children'
    Cooking_Nutrition = 'Cooking & Nutrition'
    Crafts_Hobbies = 'Crafts & Hobbies'
    Egypt = 'Egypt'
    History_Politics = 'History & Politics'
    Literature_Fiction = 'Literature & Fiction'
    Mind_Body = 'Mind & Body'
    Reference = 'Reference'
    Religion = 'Religion'
    Society = 'Society'
    Sports = 'Sports'
    Teens = 'Teens'
    Travel = 'Travel'

    Classification_Choice = (
        (Art_Design, 'Art & Design'),
        (Biographies, 'Biographies'),
        (Business, 'Business'),
        (Children, 'Children'),
        (Cooking_Nutrition, 'Cooking & Nutrition'),
        (Crafts_Hobbies, 'Crafts & Hobbies'),
        (Egypt, 'Egypt'),
        (History_Politics, 'History & Politics'),
        (Literature_Fiction, 'Literature & Fiction'),
        (Mind_Body, 'Mind & Body'),
        (Reference, 'Reference'),
        (Religion, 'Religion'),
        (Society, 'Society'),
        (Sports, 'Sports'),
        (Teens, 'Teens'),
        (Travel, 'Travel'),
    )
    classification = models.CharField(
        max_length=50,
        choices=Classification_Choice,
        default=Art_Design,
    )

    img = models.ImageField(upload_to='books/', default='books/no.png')
    img_inside = models.ImageField(upload_to='books/', default='books/no_inside.png')
    is_available = models.BooleanField(default=True)
    book_date = models.DateTimeField(default=datetime.now, blank=True)
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Book'


