import os
from decouple import config
from unipath import Path
import dj_database_url



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True)

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]



AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]




# Application definition

INSTALLED_APPS = [
    #'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'app',     # Enable the inner app
    'mptt',    # https://django-mptt.readthedocs.io/en/latest/index.html
    'mapbox_location_field',  # https://github.com/simon-the-shark/django-mapbox-location-field
    # Third Party - 1) All Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount','allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'core.urls'
#LOGIN_REDIRECT_URL = "home"   # Route defined in app/urls.py
#LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



######################## location ##########################
#  https://account.mapbox.com/
MAPBOX_KEY = "pk.eyJ1IjoiZG9yb3N0a2FyIiwiYSI6ImNrbWZjenNyMjA5MGYybnMwNjRrd3BlbG8ifQ.Ytgsb2uv9XqoLK52HQ_pEw"





# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]






ACCOUNT_AUTHENTICATION_METHOD = ("username")
ACCOUNT_EMAIL_VERIFICATION = ("none")
#ACCOUNT_EMAIL_VERIFICATION = ('mandatory')
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION  = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
EMAIL_CONFIRMATION_SIGNUP = True
ACCOUNT_EMAIL_REQUIRED =True
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'
ACCOUNT_LOGOUT_ON_GET =False
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = (ACCOUNT_EMAIL_REQUIRED)
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_AVATAR_SUPPORT = ( 'avatar' in INSTALLED_APPS)
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'nimadorostkar97@gmail.com'
EMAIL_HOST_PASSWORD = 'uwiuhrmphbdhysyn'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'






# Required for all-auth
SITE_ID = 1


# Provider specific settings for all-auth apps
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': str(os.getenv('FACEBOOK_CLIENT_ID')),
            'secret': str(os.getenv('FACEBOOK_SECRET_KEY')),
            'key': ''
        }
    },
    'google': {
        'APP': {
            'client_id': '1001926169320-i749100fk3578u1opss736rbt1nghnik.apps.googleusercontent.com',
            'secret': 'mKqAB7SKk4C-ck8FIIuQlE3l',
            'key': ''
        }
    },
    'twitter': {
        'APP': {
            'client_id': str(os.getenv('TWITTER_CLIENT_ID')),
            'secret': str(os.getenv('TWITTER_SECRET_KEY')),
            'key': ''
        }
    }
}





# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)
#############################################################
#############################################################
