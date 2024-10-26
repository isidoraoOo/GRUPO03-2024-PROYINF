from django.db import models

# Create your models here.

class Sources(models.Model):
    link = models.URLField(
        verbose_name="link de la fuente",
        unique = True,  # Ensures the link is unique
        blank = False,  # Cannot be empty
        null = False    # Cannot be null
    )
    description = models.CharField(
        max_length = 255,
        verbose_name = "Descripcion",
        blank = True,  # Optional field
        null = True    # Can be null
    )
    created_at = models.DateTimeField(
        auto_now_add = True,  # Automatically set the field to now when the object is first created
        verbose_name = "Fecha de creación"
    )

    def __str__(self):
        return self.link