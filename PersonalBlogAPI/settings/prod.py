import django_heroku
from PersonalBlogAPI.settings.base import *


ALLOWED_HOSTS = ['https://into-tomorrow.herokuapp.com/']

# Turn off debug for 
DEBUG = False

CORS_ALLOW_CREDENTIAL = True # Allow Cookies

CORS_ORIGIN_WHITELIST = (
    # Only allow specific front end to talk to this back end
    'https://into-tomorrow.herokuapp.com/'
)

# Activate django_herkou to allow connection to Heroku and establish Postgres Database

django_heroku.settings(locals())