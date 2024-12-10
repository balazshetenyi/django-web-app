from django.db import models


class Band(models.Model):
    name = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=100)