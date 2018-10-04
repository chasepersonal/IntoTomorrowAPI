from django.test import TestCase
from blogAPI.models import Photo
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

class TestPhoto(TestCase):
    # Test that the description of the photo saves
    def test_photo_saves_description(self):
        # album_id needed as it is a required field and needed to test the saved description
        photoDescription = Photo(album_id = '1', description='This is a description of the photo')
        photoDescription.save()
        self.assertEqual(photoDescription.description, 'This is a description of the photo')