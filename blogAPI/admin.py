from django.contrib import admin
from .models import Blog, Page

# Register Blog model to be used with Django Admin

admin.site.register(Blog)
admin.site.register(Page)
