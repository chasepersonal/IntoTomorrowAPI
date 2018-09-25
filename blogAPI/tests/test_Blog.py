from django.test import TestCase
from blogAPI.models import Blog
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

class TestBlog(TestCase):
    def setUp(self):
        # Define test variables to be used throughout the tests
        self.client = APIClient()
        # Needed in set up for query calls
        self.blogData = {'author': 'Test Person', 'title': 'New Blog Post', 'text': 'Content for this post'}
        self.blogResponse = self.client.post(
            reverse('posts'),
            self.blogData,
            format="json"
        )

    def test_save_appends_slug_blog(self):
        # Call blog object and save a title
        # Call created slug to see if slugify works
        newPost = Blog(title='New Blog Post')
        newPost.save()
        self.assertEqual(newPost.slug, 'new-blog-post')

    def test_save_shortens_text_to_summary(self):
        # Call blog object and save some text
        newPost = Blog(text='This is some pretty lengthy text that will probably have to be shortend as it is really long and taking up a lot of the screen and running on for what seems like forever')
        newPost.save()
        self.assertEqual(newPost.summary, 'This is some pretty lengthy text that will probably have to be shortend as it is really long and taking...')

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

    def test_api_can_retreive_a_blog_post_using_slug(self):
        # retrieve a blog post using the slug
        blogPost = Blog.objects.get()
        blogReturn = self.client.get(
            reverse('blog-details',
            kwargs={'slug': blogPost.slug}), format="json"
            )
        # Confirm HTTP response and that the response equals the SQL call
        self.assertEqual(blogReturn.status_code, 200)
        self.assertContains(blogReturn, blogPost)