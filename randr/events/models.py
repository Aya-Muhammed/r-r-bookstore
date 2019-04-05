from django.db import models
from datetime import date, time


class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=time)
    location = models.CharField(max_length=50)
    about = models.TextField()
    img = models.ImageField(upload_to='events/', default='events/no.png')
    img_inside = models.ImageField(upload_to='events/', default='events/no_inside.png')

    objects = models.Manager()

    def __str__(self):
        return self.name
