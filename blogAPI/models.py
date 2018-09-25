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
    summary = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    
    # When saving, override save function to set slug
    def save(self, *args, **kwargs):
        # If id is not set, save slug and summaryu
        if not self.id:
            # Use slugify method to transform title into slug
            self.slug = slugify(self.title)
            # Split text between 1st and 20th words
            # Then join together to create the summary
            self.summary = " ".join(self.text.split()[0:20])
            # Add ellipsis at end to indicate summary
            self.summary += '...'
        # Calls super class to instatiate the new save
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        # Return human readable version
        return "{}".format(self.title)

class Page(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # If id does not exist, set title to lowercase when saving
        if not self.id:
            self.slug = slugify(self.title)
        # Calls super class to instatiate the new save
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        # Return human readable version
        return "{}".format(self.title)

# Variable definitions for Album class
class Album(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(blank=True)
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
    image = models.ImageField(blank=True)

