from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
         return '{} {}'.format(self.name,self.pk)

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)
