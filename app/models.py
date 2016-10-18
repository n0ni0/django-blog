from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('app.Category')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title