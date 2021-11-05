from django.db import models


class Simplex(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.CharField(max_length=500)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

