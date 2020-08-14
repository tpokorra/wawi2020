from django.db import models


class Location(models.Model):
    name_text = models.CharField(max_length=200)
    descr_text = models.TextField()

    def __str__(self):
        return self.name_text


class Item(models.Model):
    name_text = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    descr_text = models.TextField()
    number_text = models.CharField(max_length=200)
    count = models.IntegerField(default=1)
    photo = models.TextField()

    def __str__(self):
        return self.name_text
