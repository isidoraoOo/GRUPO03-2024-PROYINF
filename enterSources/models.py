# models.py

from django.db import models

# Create your models here.

class Sources(models.Model):
    link = models.URLField(
        verbose_name="link de la fuente",
        unique = True,  # Ensures the link is unique
        blank = False,  # Cannot be empty
        null = False    # Cannot be null
    )

    resumen = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add = True,  # Automatically set the field to now when the object is first created
        verbose_name = "Fecha de creación"
    )

    def __str__(self):
        return self.link

class Categories(models.Model):
    category = models.CharField(
        max_length = 255,
        verbose_name = "Categoria. Si pertenece a mas de una, separalas por una coma",
        blank = False, # Cannot be empty
        null = False # Cannot be empty
    )

    def __str__(self):
        return "Categoria/s: %s." % (self.category)

#  Fixes ManyToMany relationship
class Cat_x_Source(models.Model):
    source = models.ForeignKey(Sources, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return "La fuente %s pertenece a la categoria/s %s" % (self.source.link, self.category.category)