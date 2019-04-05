from django.db import models


class Accessory(models.Model):
    img = models.ImageField(upload_to='accessories/', default='accessories/no.png')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img_inside1 = models.ImageField(upload_to='accessories/', default='accessories/no.png', blank=True)
    img_inside2 = models.ImageField(upload_to='accessories/', default='accessories/no.png', blank=True)
    img_inside3 = models.ImageField(upload_to='accessories/', default='accessories/no.png', blank=True)
    title = models.CharField(max_length=50)
    overview = models.TextField(blank=True)
    description = models.TextField()

    def overview_lines(self):
        return filter(None, (line.strip() for line in self.overview.splitlines()))

    Bookmarks = 'Bookmarks'
    Book_covers = 'Book covers'
    Bookend = 'Bookend'
    Book_stands = 'Book stands'
    Book_light = 'Book light'
    Notebooks = 'Notebooks'

    Category_Choice = (
        (Bookmarks, 'Bookmarks'),
        (Book_covers, 'Book covers'),
        (Bookend, 'Bookend'),
        (Book_stands, 'Book stands'),
        (Book_light, 'Book light'),
        (Notebooks, 'Notebooks'),
    )

    category = models.CharField(
        max_length=50,
        choices=Category_Choice,
        default=Bookmarks,
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Accessory'
