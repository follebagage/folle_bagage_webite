from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    photo = models.ImageField(upload_to='products/photos/')
    description = models.TextField()
    making_video = models.FileField(upload_to='products/videos/')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
