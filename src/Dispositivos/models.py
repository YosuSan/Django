from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Movil(models.Model):
    marca = models.CharField(max_length=20, blank=False)
    modelo = models.CharField(max_length=50, blank=False)
    SO = models.CharField(max_length=10)
    version_SO = models.IntegerField()

    def __unicode__(self):  # Python 2
        return self.marca

    def __str__(self):  # Python 3
        return self.marca
