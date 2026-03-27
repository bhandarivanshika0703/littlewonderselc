from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ======================
# SECURITY
# ======================
SECRET_KEY = 'django-insecure-(x&+!t37j_3e%j3(ogad5%^7q#&sgy2h70iigs$k9mt()dw@t+'

DEBUG = False  # Keep True for now (local testing)

ALLOWED_HOSTS = [ "littlewonderselc.onrender.com",
    "localhost",
    "127.0.0.1"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ======================
# APPLICATIONS
# ======================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
       'cloudinary',
    'cloudinary_storage',
]

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
      'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'project.urls'


# ======================
# TEMPLATES
# ======================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # ✅ FIXED
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'project.wsgi.application'


# ======================
# DATABASE
# ======================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ======================
# PASSWORD VALIDATION
# ======================
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


# ======================
# INTERNATIONAL
# ======================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ======================
# STATIC FILES
# ======================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ FIXED (NO HASHING ISSUE)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ======================
# MEDIA FILES
# ======================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CSRF_TRUSTED_ORIGINS = [
    "https://littlewonderselc.onrender.com"
]


# ======================
# DEFAULT PRIMARY KEY
# ======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'