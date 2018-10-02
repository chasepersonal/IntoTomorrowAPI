from PersonalBlogAPI.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Collect media files locally and save them in a media folder
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL for media collection
MEDIA_URL = '/media/'