"""
WSGI config for freeMECPlatform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.sessions.backends.db import SessionStore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freeMECPlatform.settings')

application = get_wsgi_application()


