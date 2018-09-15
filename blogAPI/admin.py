from django.contrib import admin
from .models import Blog, Page, Photo

# Register Blog model to be used with Django Admin

class InlinePhoto(admin.TabularInline):
    model = Photo

class PageAdmin(admin.ModelAdmin):
    inlines = [InlinePhoto]

admin.site.register(Blog)
admin.site.register(Page, PageAdmin)
admin.site.register(Photo)
