from django.contrib import admin
from .models import Blog, Page, Photo, Album

# Register Blog model to be used with Django Admin

class InlinePhoto(admin.TabularInline):
    model = Photo

class AlbumAdmin(admin.ModelAdmin):
    inlines = [InlinePhoto]

admin.site.register(Blog)
admin.site.register(Page)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)

