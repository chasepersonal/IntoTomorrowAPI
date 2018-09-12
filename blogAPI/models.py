# Import Utilities

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import forms
from django.template.defaultfilters import slugify
import uuid

# Variable definitions for Blog class

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="name")
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="name")
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Return human readable version
        return "{}".format(self.title)

class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    image = models.ImageField()

