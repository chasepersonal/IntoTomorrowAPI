# URL's for API

from django.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogCreateView, BlogDetailsView, PageCreateView, PageDetailsView, PhotoDetailsView, PhotoCreateView, AlbumCreateView, AlbumDetailsView

# Set patters for specific urls
urlpatterns = {
    path('posts', BlogCreateView.as_view(), name="posts"),
    path('posts/<slug>', BlogDetailsView.as_view(), name="blog-details"),
    path('pages', PageCreateView.as_view(), name="pages"),
    path('pages/<slug>', PageDetailsView.as_view(), name="page-details"),
    path('albums', AlbumCreateView.as_view(), name="albums"),
    path('albums/<slug>', AlbumDetailsView.as_view(), name="album-details"),
    path('photo', PhotoCreateView.as_view(), name="photo"),
    path('photo/<pk>', PhotoDetailsView.as_view(), name="photo-details"),
}

# Format url based on url patterns
# Allows specification of format when URL's are used
urlpatterns = format_suffix_patterns(urlpatterns)