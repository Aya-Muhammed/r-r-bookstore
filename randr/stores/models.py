from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    img = models.ImageField(upload_to='stores/', default='stores/no.png')

    objects = models.Manager()

    def __str__(self):
        return self.name
