# URL's for API

from django.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogCreateView, BlogDetailsView, PageCreateView, PageDetailsView, PhotoDetailsView, AlbumCreateView

# Set patters for specific urls
urlpatterns = {
    path('posts', BlogCreateView.as_view(), name="posts"),
    path('posts/<slug>', BlogDetailsView.as_view(), name="blog-details"),
    path('pages', PageCreateView.as_view(), name="pages"),
    path('album/<slug>', BlogDetailsView.as_view(), name="album-details"),
    path('album', AlbumCreateView.as_view(), name="album"),
    path('photo', PhotoDetailsView.as_view(), name="photo"),
    path('photo/<pk>', PhotoDetailsView.as_view(), name="photo-details"),
    path('pages/<title>', PageDetailsView.as_view(), name="pages-details")
}

# Format url based on url patterns
# Allows specification of format when URL's are used
urlpatterns = format_suffix_patterns(urlpatterns)