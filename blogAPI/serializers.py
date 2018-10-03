from rest_framework import serializers, fields
from .models import *

# Create serializer to map models into JSON format
# Will make data transmission easier
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'author', 'title', 'text', 'summary', 'slug', 'created_date', 'modified_date')
        read_only_fields = ('summary', 'slug', 'created_date', 'modified_date')

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'author', 'title', 'slug', 'header', 'text', 'created_date', 'modified_date')
        read_only_fields = ('slug', 'header', 'created_date', 'modified_date')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'album', 'image', 'created_date', 'description')

class AlbumSerializer(serializers.ModelSerializer):

    photo = PhotoSerializer(many=True)

    class Meta:
        model = Album
        fields = ('id', 'author', 'title', 'summary', 'slug', 'created_date', 'modified_date', 'photo')

    # Will write data to nested serializer
    def create(self, validated_data):
        photos_data = validated_data.pop('photo')
        album = Album.objects.create(**validated_data)
        for photo_data in photos_data:
            Photo.objects.create(**photo_data)
        return album