from django.test import TestCase
from .models import Blog, Page, Album
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

class TestBlog(TestCase):
    def setUp(self):
        # Define test variables to be used throughout the tests
        self.client = APIClient()
        # Needed in set up for query calls
        self.blogData = {'author': 'Test Person', 'title': 'New Blog Post', 'text': 'Content for this post'}
        self.pageData = {'author': 'Test Person', 'title': 'New Page', 'header': 'What am I doing?', 'text': 'This is a new page'}
        self.albumData = {'author': 'Test Person', 'title': 'New Album', 'text': 'This is a new album', 'photo': []}
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
        self.albumResponse = self.client.post(
            reverse('albums'),
            self.albumData,
            format="json"
        )

    def test_save_appends_slug_blog(self):
        # Call blog object and save a title
        # Call created slug to see if slugify works
        newPost = Blog(title='New Blog Post')
        newPost.save()
        self.assertEqual(newPost.slug, 'new-blog-post')

    def test_api_can_create_blog_post(self):
        # Test that a blog post will be created
        self.assertEqual(self.blogResponse.status_code, 201)

    def test_api_can_retreive_all_blog_posts(self):
        
        blogPost = Blog.objects.get()
        blogReturn = self.client.get(
            reverse('posts'),
            format="json"
            )
        # Confirm HTTP response and that the response equals the SQL call
        self.assertEqual(blogReturn.status_code, 200)
        self.assertContains(blogReturn, blogPost)

    def test_api_can_retreive_a_blog_post(self):
        # retrieve a blog post using the slug
        blogPost = Blog.objects.get()
        blogReturn = self.client.get(
            reverse('blog-details',
            kwargs={'slug': blogPost.slug}), format="json"
            )
        # Confirm HTTP response and that the response equals the SQL call
        self.assertEqual(blogReturn.status_code, 200)
        self.assertContains(blogReturn, blogPost)

    def test_api_can_create_page(self):
        # Test that a page will be created
        self.assertEqual(self.pageResponse.status_code, 201)

    def test_api_can_retreive_all_pages(self):
        # Retrieve all pages
        page = Page.objects.get()
        pageReturn = self.client.get(
            reverse('pages'),
            format="json"
            )
        # Confirm HTTP response and that the response equals the SQL call
        self.assertEqual(pageReturn.status_code, 200)
        self.assertContains(pageReturn, page)

    def test_api_can_retreive_a_page(self):
        # Retrieve a page using it's title
        page = Page.objects.get()
        pageReturn = self.client.get(
            reverse('page-details',
            kwargs={'title': page.title}), format="json"
            )
        # Confirm HTTP response and that the response equals the SQL call
        self.assertEqual(pageReturn.status_code, 200)
        self.assertContains(pageReturn, page)

    def test_api_can_create_album(self):
        self.assertEqual(self.albumResponse.status_code, 201)

    def test_api_can_retreive_an_album(self):
        # Retrieve an album using it's slug
        albumPost = Album.objects.get()
        albumReturn = self.client.get(
            reverse('album-details',
            kwargs={'slug': albumPost.slug}), format="json"
            )
        # Confirm HTTP response and that the response equals the SQL call
        self.assertEqual(albumReturn.status_code, 200)
        self.assertContains(albumReturn, albumPost)

    def test_save_appends_slug_album(self):
        # Call blog object and save a title
        # Call created slug to see if slugify works
        newAlbum = Album(title='New Jersey')
        newAlbum.save()
        self.assertEqual(newAlbum.slug, 'new-jersey')