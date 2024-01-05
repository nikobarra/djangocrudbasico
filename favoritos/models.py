from django.db import models


class Favoritos(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    url = models.URLField()
