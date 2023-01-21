from decouple import config

from .base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
