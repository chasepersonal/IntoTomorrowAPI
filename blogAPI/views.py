from django.shortcuts import render
from rest_framework import generics
from .models import Blog, Page, Photo, Album
from .serializers import BlogSerializer, PageSerializer, PhotoSerializer, AlbumSerializer

# View to allow API calls for Blog

# View for POST for Blog, Page, Photo, and Author Models
class BlogCreateView(generics.ListCreateAPIView):
    # Defines create behavior for API
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # Function to aid in creation of new posts
    # Will use serializer when post is created
    def perform_post(self, serializer):
    # Save post data when new blog post is created
        serializer.save()

class PhotoCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_post(self, serializer):
        serializer.save()

class PageCreateView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def perform_post(self, serializer):
        serializer.save()

class AlbumCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_post(self, serializer):
        serializer.save()

# View for GET, PUT, and DELETE requests for Blog

class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'

class PageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'

class PhotoDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class AlbumDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    lookup_field = 'slug'