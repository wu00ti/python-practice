import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")

from django.core.wagi import get_wsgi_application
application = get_wsgi_application()
