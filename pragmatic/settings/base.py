"""
Django settings for pragmatic project (Render-ready).

Base settings. For local/dev/prod overrides, use a separate module or env vars.
"""

from pathlib import Path
import os
import environ
from django.contrib.messages import constants as messages
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # project root (where manage.py lives)


env = environ.Env(
    DEBUG=(bool, False),
)
# Load .env if present (safe on Render; no-op if file missing)
environ.Env.read_env()

# SECURITY
SECRET_KEY = env("SECRET_KEY", default="CHANGE_ME_IN_ENV")  # set in Render → Environment
DEBUG = env("DEBUG", default=False)

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["localhost", "127.0.0.1", ".onrender.com", ".render.com"],
)

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",  # ← collectstatic 제공

    # 3rd-party
    "bootstrap4",

    # Local apps
    "accountapp",
    "profileapp",
    "articleapp",
    "commentapp",
    "projectapp",
    "subscribeapp",
    "likeapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ← 정적파일 서빙(렌더)
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

ROOT_URLCONF = "pragmatic.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "pragmatic.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # where collectstatic dumps files

# Optional: additional source dirs for static (safe if folder exists)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# WhiteNoise: compressed + hashed filenames (cache-friendly)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGOUT_REDIRECT_URL = reverse_lazy("accountapp:login")

# ------------------------------------------------------------------------------
# Django 3.2 default PK type
# ------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
