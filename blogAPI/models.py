# Import Utilities

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import forms
from django.template.defaultfilters import slugify

# Variable definitions for Blog class
class Blog(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    
    # When saving, override save function to set slug
    def save(self, *args, **kwargs):
        # Set slug once
        if not self.id:
            self.slug = slugify(self.title)
        # Calls super class to instatiate the new save
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        # Return human readable version
        return "{}".format(self.title)

class Page(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # Return human readable version
        return "{}".format(self.title)

# Variable definitions for Album class
class Album(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)

    # When saving, override save function to set slug
    def save(self, *args, **kwargs):
        # Set slug once
        if not self.id:
            self.slug = slugify(self.title)
        # Calls super class to instatiate the new save
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        # Return human readable version
        return "{}".format(self.title)

# Variable definitions for the Photo class
class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photo', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField()

