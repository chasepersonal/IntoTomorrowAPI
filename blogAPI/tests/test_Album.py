from django.test import TestCase
from blogAPI.models import Album
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

class TestAlbum(TestCase):
    def setUp(self):
        # Define test variables to be used throughout the tests
        self.client = APIClient()
        self.albumData = {'author': 'Test Person', 'title': 'New Album', 'text': 'This is a new page', 'photo': []}
        self.albumResponse = self.client.post(
            reverse('albums'),
            self.albumData,
            format="json"
        )

    def test_api_can_create_album(self):
        self.assertEqual(self.albumResponse.status_code, 201)

    def test_save_appends_slug_album(self):
        # Call blog object and save a title
        # Call created slug to see if slugify works
        newAlbum = Album(title='New Jersey')
        newAlbum.save()
        self.assertEqual(newAlbum.slug, 'new-jersey')

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