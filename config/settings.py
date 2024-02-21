import os
from datetime import timedelta
from pathlib import Path

from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-3ith&zg!8mf1*l2)rn#r(1_ugm90+bk)a(b-znmnrc74br11%h"

DEBUG = True

ALLOWED_HOSTS = []

ALLAUTH_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

LOCAL_APPS = [
    "apps.todo.apps.TodoConfig",
    "apps.authentication.apps.AuthenticationConfig",
]

THIRD_PATRY_APPS = [
    "rest_framework", "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular", "rosetta", "corsheaders", *ALLAUTH_APPS
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    *LOCAL_APPS,
    *THIRD_PATRY_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "allauth.account.middleware.AccountMiddleware",
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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "database/db.sqlite3"),
    }
}

AUTH_USER_MODEL = "authentication.User"

ACCOUNT_AUTHENTICATION_METHOD = "email"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USER_MODEL_USERNAME_FIELD = None

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "60/minute",
        "user": "1000/minute",
    },
    "DEFAULT_SCHEMA_CLASS":
    "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS":
    "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE":
    10,
    "DEFAULT_METADATA_CLASS":
    "config.metadata.CustomMetaData",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME":
    timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME":
    timedelta(days=60),
    "ROTATE_REFRESH_TOKENS":
    True,
    "BLACKLIST_AFTER_ROTATION":
    True,
    "UPDATE_LAST_LOGIN":
    True,
    "ALGORITHM":
    "HS256",
    "VERIFYING_KEY":
    "",
    "AUDIENCE":
    None,
    "ISSUER":
    None,
    "JSON_ENCODER":
    None,
    "JWK_URL":
    None,
    "LEEWAY":
    0,
    "AUTH_HEADER_TYPES": ("Bearer", ),
    "AUTH_HEADER_NAME":
    "HTTP_AUTHORIZATION",
    "USER_ID_FIELD":
    "id",
    "USER_ID_CLAIM":
    "user_id",
    "USER_AUTHENTICATION_RULE":
    "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken", ),
    "TOKEN_TYPE_CLAIM":
    "token_type",
    "TOKEN_USER_CLASS":
    "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM":
    "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM":
    "refresh_exp",
    "SLIDING_TOKEN_LIFETIME":
    timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME":
    timedelta(days=1),
    "TOKEN_OBTAIN_SERIALIZER":
    "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER":
    "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER":
    "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER":
    "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER":
    "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER":
    "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Todo API Project",
    "DESCRIPTION": "API For Todo Application",
    "VERSION": "1.0.0",
}

CORS_ALLOW_ALL_ORIGINS = True

LANGUAGE_CODE = "en-us"

LANGUAGES = (
    ("en", _("English")),
    ("fa", _("Persian")),
)

LOCALE_PATHS = (os.path.join(BASE_DIR / "locale/"), )

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
