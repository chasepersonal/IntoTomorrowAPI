from rest_framework import serializers
from .models import Blog, Page

# Create serializer to map models into JSON format
# Will make data transmission easier
class AuthorSerializer(serialzers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'author', 'title', 'text', 'slug', 'created_date', 'modified_date')
        read_only_fields = ('slug', 'created_date', 'modified_date')

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'author', 'title', 'header', 'text', 'created_date', 'modified_date')
        read_only_fields = ('header', 'created_date', 'modified_date')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'blogId', 'pageId', 'image' )