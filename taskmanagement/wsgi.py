"""
WSGI config for taskmanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise # Import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanagement.settings')

application = get_wsgi_application()

# Wrap your Django WSGI application with WhiteNoise
# This tells WhiteNoise where to find the collected static files.
# '..' is used to go up one directory from the 'taskmanagement' project folder
# to the root of your repository where 'staticfiles' should reside after collectstatic.
application = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'staticfiles'))

# Vercel often looks for a variable named 'app' as the WSGI callable.
app = application
