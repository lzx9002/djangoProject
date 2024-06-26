"""
WSGI config for djangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import threading

from django.core.wsgi import get_wsgi_application
from djangoProject import cpuUsage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

application = get_wsgi_application()

thread = threading.Thread(target=cpuUsage.cpuUsableRecorder)
thread.start()
