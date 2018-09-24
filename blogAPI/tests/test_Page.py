from django.test import TestCase
from blogAPI.models import Page
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

class TestPage(TestCase):
    def setUp(self):
        # Define test variables to be used throughout the tests
        self.client = APIClient()
        self.pageData = {'author': 'Test Person', 'title': 'New Page', 'header': 'What am I doing?', 'text': 'This is a new page'}
        self.pageResponse = self.client.post(
            reverse('pages'),
            self.pageData,
            format="json"
        )

    # Test page funcitonality
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
