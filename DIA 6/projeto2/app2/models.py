from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    population = models.IntegerField()
    flag_url = models.URLField()

    def __str__(self):
        return self.name
