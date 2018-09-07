from django.test import TestCase
from .models import Blog, Page
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

class TestBlog(TestCase):
    def setUp(self):
        # Define test variables to be used throughout the tests
        self.client = APIClient()
        # Needed in set up for query calls
        self.blogData = {'author': 'Test Person', 'title': 'New Blog Post', 'text': 'Content for this post'}
        self.pageData = self.blog_data = {'author': 'Test Person', 'title': 'New Page', 'text': 'This is a new page'}
        self.blogResponse = self.client.post(
            reverse('posts'),
            self.blogData,
            format="json"
        )
        self.pageResponse = self.client.post(
            reverse('pages'),
            self.pageData,
            format="json"
        )

    def test_save_appends_slug(self):
        # Call blog object and save a title
        # Call created slug to see if slugify works
        newPost = Blog(title='New Blog Post')
        newPost.save()
        self.assertEqual(newPost.slug, 'new-blog-post')

    def test_api_can_create_blog_post(self):
        # Test that a blog post will be created
        self.assertEqual(self.blogResponse.status_code, 201)
    
    def test_api_can_retreive_a_blog_post(self):
        # retrieve a blog post using the slug
        blogPost = Blog.objects.get()
        blogResponse = self.client.get(
            reverse('blog-details',
            kwargs={'slug': blogPost.slug}), format="json"
            )
        # Confirm HTTP response and that the response equals the SQL call
        self.assertEqual(blogResponse.status_code, 200)
        self.assertContains(blogResponse, blogPost)

    def test_api_can_create_page(self):
        # Test that a page will be created
        self.assertEqual(self.pageResponse.status_code, 201)

    def test_api_can_retreive_a_page(self):
        # retrieve a blog post using the slug
        page = Page.objects.get()
        pageResponse = self.client.get(
            reverse('pages-details',
            kwargs={'title': page.title}), format="json"
            )
        # Confirm HTTP response and that the response equals the SQL call
        self.assertEqual(pageResponse.status_code, 200)
        self.assertContains(pageResponse, page)
