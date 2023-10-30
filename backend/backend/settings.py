"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta
import dj_database_url  # import database when deploying
from corsheaders.defaults import default_headers

from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-!c+651yr@%88v&!mrvsa9vmq8!7py4@f2nysaz##x+=s@vtg9$'
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")
# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"


# ALLOWED_HOSTS = ['localhost']

ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    'https://reactjs-ecommerce-render.onrender.com',
    'http://localhost:3000',
    'http://localhost:8000',
    'https://website-django-react.vercel.app',
    'https://django-ecommerce-render.onrender.com',
    'https://website-django-react-a11e.vercel.app',
    'https://render.com',
    'http://13.228.225.19',
    'http://18.142.128.26',
    'http://54.254.162.138',
    # os.environ.get("FRONTEND_URL")
]

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURE_SSL_REDIRECT = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    # 3rd party apps
    'rest_framework',
    'corsheaders',
]

# simple JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=2000),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1500),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": os.environ.get("SECRET_KEY"),
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware', # add whitenoise middleware | python manage.py collectstatic
]


ROOT_URLCONF = 'backend.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# database_url = os.environ.get("DATABASE_URL")
# DATABASES['default'] = dj_database_url.parse(database_url)


# Password validationdpg-ckn14611rp3c73f2dmjg-a
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_DIRS = [
    BASE_DIR/'static',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ALLOW_HEADERS = list(default_headers) + [
#     "WWW-Authenticate",
#     "Authorization",
#     "Proxy-Authenticate",
#     "Proxy-Authorization",
#     "Age",
#     "Cache-Control",
#     "Clear-Site-Data",
#     "Expires",
#     "Pragma",
#     "Warning",
#     "Accept-CH",
#     "Accept-CH-Lifetime",
#     "Sec-CH-UA",
#     "Sec-CH-UA-Arch",
#     "Sec-CH-UA-Bitness",
#     "Sec-CH-UA-Full-Version",
#     "Sec-CH-UA-Full-Version-List",
#     "Sec-CH-UA-Mobile",
#     "Sec-CH-UA-Model",
#     "Sec-CH-UA-Platform",
#     "Sec-CH-UA-Platform-Version",
#     "Content-DPR",
#     "Device-Memory",
#     "DPR",
#     "Viewport-Width",
#     "Width",
#     "Downlink",
#     "ECT",
#     "RTT",
#     "Save-Data",
#     "Last-Modified",
#     "ETag",
#     "If-Match",
#     "If-None-Match",
#     "If-Modified-Since",
#     "If-Unmodified-Since",
#     "Vary",
#     "Connection",
#     "Keep-Alive",
#     "Accept",
#     "Accept-Encoding",
#     "Accept-Language",
#     "Expect",
#     "Max-Forwards",
#     "Cookie",
#     "Set-Cookie",
#     "Access-Control-Allow-Origin",
#     "Access-Control-Allow-Credentials",
#     "Access-Control-Allow-Headers",
#     "Access-Control-Allow-Methods",
#     "Access-Control-Expose-Headers",
#     "Access-Control-Max-Age",
#     "Access-Control-Request-Headers",
#     "Access-Control-Request-Method",
#     "Origin",
#     "Timing-Allow-Origin",
#     "Content-Disposition",
#     "Content-Length",
#     "Content-Type",
#     "Content-Encoding",
#     "Content-Language",
#     "Content-Location",
#     "Forwarded",
#     "X-Forwarded-For",
#     "X-Forwarded-Host",
#     "X-Forwarded-Proto",
#     "Via",
#     "Location",
#     "From",
#     "Host",
#     "Referer",
#     "Referrer-Policy",
#     "User-Agent",
#     "Allow",
#     "Server",
#     "Accept-Ranges",
#     "Range",
#     "If-Range",
#     "Content-Range",
#     "Cross-Origin-Embedder-Policy",
#     "Cross-Origin-Opener-Policy",
#     "Cross-Origin-Resource-Policy",
#     "Content-Security-Policy",
#     "Content-Security-Policy-Report-Only",
#     "Expect-CT",
#     "Feature-Policy",
#     "Origin-Isolation",
#     "Strict-Transport-Security",
#     "Upgrade-Insecure-Requests",
#     "X-Content-Type-Options",
#     "X-Download-Options",
#     "X-Frame-Options",
#     "X-Permitted-Cross-Domain-Policies",
#     "X-Powered-By",
#     "X-XSS-Protection",
#     "Sec-Fetch-Site",
#     "Sec-Fetch-Mode",
#     "Sec-Fetch-User",
#     "Sec-Fetch-Dest",
#     "Service-Worker-Navigation-Preload",
#     "Last-Event-ID",
#     "NEL",
#     "Ping-From",
#     "Ping-To",
#     "Report-To",
#     "Transfer-Encoding",
#     "TE",
#     "Trailer",
#     "Sec-WebSocket-Key",
#     "Sec-WebSocket-Extensions",
#     "Sec-WebSocket-Accept",
#     "Sec-WebSocket-Protocol",
#     "Sec-WebSocket-Version",
#     "Accept-Push-Policy",
#     "Accept-Signature",
#     "Alt-Svc",
#     "Date",
#     "Early-Data",
#     "Large-Allocation",
#     "Link",
#     "Push-Policy",
#     "Retry-After",
#     "Signature",
#     "Signed-Headers",
#     "Server-Timing",
#     "Service-Worker-Allowed",
#     "SourceMap",
#     "Upgrade",
#     "X-DNS-Prefetch-Control",
#     "X-Firefox-Spdy",
#     "X-Pingback",
#     "X-Requested-With",
#     "X-Robots-Tag",
#     "X-UA-Compatible",
#     "ContentType",
#     "Content-type",
#     "content-type",
#     "contenttype",
#     "contentType",


#     "accept",
#     "authorization",
#     "dnt",
#     "origin",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",

#     "accept-encoding",

#     "Contentype",
# ]
