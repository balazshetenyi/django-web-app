from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
        
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2020)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    
    class Type(models.TextChoices):
        RECORDS = 'Records'
        CLOTHING = 'Clothing'
        POSTERS = 'Posters'
        OTHER = 'Other'
        
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    type = models.CharField(choices=Type.choices, max_length=100)