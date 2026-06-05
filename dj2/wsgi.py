"""
WSGI config for dj2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

# Python 3.10+ compatibility shims for Django 2.0
import util.compat

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj2.settings")

application = get_wsgi_application()
