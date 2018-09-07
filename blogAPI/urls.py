# URL's for API

from django.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogCreateView, BlogDetailsView, PageCreateView, PageDetailsView

# Set patters for specific urls
urlpatterns = {
    path('posts/', BlogCreateView.as_view(), name="posts"),
    path('posts/<slug>/', BlogDetailsView.as_view(), name="blog-details"),
    path('pages/', PageCreateView.as_view(), name="pages"),
    path('pages/<title>', PageDetailsView.as_view(), name="pages-details")
}

# Format url based on url patterns
# Allows specification of format when URL's are used
urlpatterns = format_suffix_patterns(urlpatterns)