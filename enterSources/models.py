from django.db import models

# Create your models here.

class Sources(models.Model):
    link = models.URLField()