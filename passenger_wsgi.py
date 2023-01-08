import os
import sys


sys.path.insert(0, os.path.dirname(__file__))
from django.core.wsgi import get_wsgi_application

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    application = get_wsgi_application()