from django.shortcuts import render
from rest_framework import generics
from .models import Blog, Page, Photo
from .serializers import BlogSerializer, PageSerializer, PhotoSerializer

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

class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'

# View for GET, PUT, and DELETE requests for Blog

class PageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'title'

class PhotoDetailsView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer