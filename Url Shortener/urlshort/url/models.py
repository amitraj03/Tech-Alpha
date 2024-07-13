from django.db import models

class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=10, unique=True)
