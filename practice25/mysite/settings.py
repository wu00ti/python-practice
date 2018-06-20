import os 
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'edycnzi5)#&3+i$d^70t@81)^tp9j@t%(m)zu+bov#4r8cl@1v'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'todolist',
        )

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware'
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.message.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        )
ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION ='mysite.wsgi.application'

DATABASES = {
        'default':{
            'ENGINE':'django.db.backends.sqlite3',
            'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
            }
        }
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
