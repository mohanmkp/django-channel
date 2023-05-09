"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from myapp import consumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# application = get_asgi_application()

ws_patterns = [
    path("ws/notification/<group_name>/", consumer.Notification.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": URLRouter(ws_patterns)
})

