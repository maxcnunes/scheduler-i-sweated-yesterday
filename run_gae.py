from google.appengine.ext.webapp.util import run_wsgi_app
from scheduler import app as application

run_wsgi_app(application)