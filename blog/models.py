from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    link = models.URLField(
        unique = True,  # Ensures the link is unique
        blank = False,  # Cannot be empty
        null = False    # Cannot be null
    )
    image = models.ImageField(upload_to="blog/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title