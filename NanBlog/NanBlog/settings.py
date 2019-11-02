"""
Django settings for NanBlog project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zl-e&!p7c^@e5g^dac@&zyc6_$jx1kh)3-31565d&$#tm_wv!m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'tinymce',
    'filebrowser',
    'django.contrib.admin',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.discord',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'widget_tweaks',
    'crispy_forms',
    'django_extensions',
    'django_twilio',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'django_seed',
    'rest_framework.authtoken',
    'rest_framework_api_key',
    'django.contrib.staticfiles',
    'graphene_django',
    'blogApp.apps.BlogappConfig',
    'Contacts.apps.ContactsConfig',
    'Utilisateurs.apps.UtilisateursConfig',
    'Statistique.apps.StatistiqueConfig',
    'allConfig.apps.AllconfigConfig',
    'django_admin_generator',
    'social_django',
    'django_social_share',
]

ACCOUNT_DEFAULT_HTTP_PROTOCOL ="https"

SOCIALACCOUNT_PROVIDERS = {
    'linkedin': {
        'SCOPE': [
            'r_basicprofile',
            'r_emailaddress'
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    }
}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', 
]

ROOT_URLCONF = 'NanBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', 
                'allConfig.context_processors.get_config',
                'Statistique.context_processors.visitor_ip_address',
            ],
        },
    },
]

AUTH_USER_MODEL = 'Utilisateurs.MyUser'
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400 # 1 day in seconds
ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/'
LOGIN_REDIRECT_URL = 'index' 
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_FORMS = {'signup': 'Utilisateurs.forms.RegistrationForm'}

# redirects to /accounts/profile by default

# TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
# TWILIO_AUTH_TOKEN =  os.environ["TWILIO_AUTH_TOKEN"]
# TWILIO_DEFAULT_CALLERID =  os.environ["TWILIO_DEFAULT_CALLERID"]

WSGI_APPLICATION = 'NanBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


#############################################################################
#                                                                           #
#                         GRAPHENE CONFIGURATION                            #
#                                                                           #
#############################################################################


GRAPHENE = {
    'SCHEMA': 'NanBlog.schema.schema'
}

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 800,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

FILEBROWSER_DIRECTORY='../media_cdn'
FILEBROWSER_MAX_UPLOAD_SIZE=10485760 *100

REST_FRAMEWORK  =  { 
    "DEFAULT_PERMISSION_CLASSES" :  [ 
        "rest_framework_api_key.permissions.HasAPIKey",
    ] 
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media_cdn')
STATIC_ROOT = os.path.join(BASE_DIR, '../static_cdn')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIT_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = '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'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

FILEBROWSER_MAX_UPLOAD_SIZE=10485760 *100
