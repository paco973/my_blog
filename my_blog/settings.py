from pathlib import Path
import json
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
with open('/etc/config.json') as config_file:
    config = json.load(config_file)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '165.232.40.239']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'django_quill',

    'user_profile',
    'app',
    'dashboard'
]

# Middleware definition

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'my_blog.middleware.CurrentUserMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'my_blog.urls'

# Templates définition

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'blog',
            'USER': 'paco',
            'PASSWORD': 'Grand-Santi973',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static/'
STATIC_URL = '/static/'
STATICFILES = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

AUTH_USER_MODEL = 'user_profile.User'


INTERNAL_IPS = ["127.0.0.1"]

QUILL_CONFIG = {
    'modules': {
        'syntax': True,
        'toolbar': [
            [{'header': [1, 2, 3, 4, 5, 6, False]}],
            [{'font': []}],
            [{'size': ['8px', '10px', '12px', '14px', '16px', '18px', '20px', '24px', '28px', '32px', '36px']}],
            [{'color': []}, {'background': []}],
            [{'align': []}],
            ['bold', 'italic', 'underline', 'strike'],
            [{'script': 'sub'}, {'script': 'super'}],
            [{'indent': '-1'}, {'indent': '+1'}],
            [{'list': 'ordered'}, {'list': 'bullet'}],
            ['blockquote', 'code-block'],
            [{'direction': 'rtl'}],
            [{'header': [1, 2, 3, 4, 5, 6, False]}],
            [{'formula': []}, {'image': []}, {'video': []}, {'clean': 'clean'}],
        ],
        'imageResize': {
            'displaySize': True,
            'modules': ['Resize', 'DisplaySize', 'Toolbar'],
            'handles': {
                'corners': True,
                'center': True
            }
        },

    },
    'formats': ['header', 'font', 'size', 'bold', 'italic', 'underline', 'strike', 'script', 'list', 'blockquote', 'code-block', 'link', 'image', 'video', 'formula', 'align', 'direction', 'color', 'background'],
    'theme': 'snow',
'default': {
        'theme': 'snow',
        'toolbar': [
            [{'font': []}],
            [{'header': [1, 2, 3, 4, 5, 6, False]}],
            ['bold', 'italic', 'underline', 'strike'],
            [{'color': []}, {'background': []}],
            [{'align': []}],
            [{'list': 'ordered'}, {'list': 'bullet'}],
            ['link', 'image', 'video'],
            ['clean']
        ],
        'toolbar_options': {
            'font': [
                'Arial',
                'Helvetica',
                'Times New Roman',
                'Courier New',
                'Verdana',
                'Georgia',
                'Palatino',
                'Garamond',
                'Bookman',
                'Comic Sans MS',
                'Trebuchet MS',
                'Arial Black',
                'Impact',
                'Lucida Console',
                'Lucida Sans Unicode',
                'Tahoma'
            ]
        }
    }

}

STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
