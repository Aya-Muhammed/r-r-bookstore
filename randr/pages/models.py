from django.db import models


class Advertise(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pages/advertises', default='pages/advertises/coming_soon.png')

    def __str__(self):
        return self.title

    objects = models.Manager()

