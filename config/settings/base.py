import environ
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_STATIC = Path(__file__).resolve().parent.parent.parent

env = environ.Env()

environ.Env().read_env(os.path.join(BASE_DIR, "../.env"))

AUTH_USER_MODEL = "users.User"

BASE_APPS = [
    "django_crontab",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
]

THIRD_PARTY_APPS = [
    # rest framework
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "corsheaders",
    "phonenumber_field",
    # redis
    "django_celery_beat",
    # admin
    "django_extensions",
]

OWN_APPS = [
    # my installed apps
    "users",
    "users.secretaries",
    "users.teachers",
    "companies",
    "webhooks",
    "api",
    "api.v1",
    "utils",
    "company_assets",
    "company_assets.offices",
    "company_assets.vehicles",
    "licences",
    "permissions",
]

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = BASE_APPS + OWN_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"


STATICFILES_DIRS = [
    BASE_DIR_STATIC / "static",
]

# media

MEDIA_URL = "/media/"

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Admin
ADMIN_URL = "admin/"
ADMINS = [
    ("""Pablo Trinidad""", "pablotrinidad@ciencias.unam.mx"),
]
MANAGERS = ADMINS

# Celery
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE

HOLDED_API_KEY = env("HOLDED_API_KEY")

CELERY_BROKER_URL = env("REDIS_HOST_CELERY")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERYD_TASK_TIME_LIMIT = 5 * 60
CELERYD_TASK_SOFT_TIME_LIMIT = 60

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.BrowsableAPIRenderer",  # add this first.
        "rest_framework.renderers.JSONRenderer",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "PAGE_SIZE": 10,
}

# Email
# EMAIL_BACKEND = env(
#    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
# )
