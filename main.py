from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

from google.appengine.ext import ndb

from flask import redirect, url_for, request


class Speed():
	site     = ndb.StringProperty(required=True)
	ping     = ndb.StringProperty()
	download = ndb.FloatProperty()
	upload   = ndb.FloatProperty()


@app.route('/')
def hello():
    """Return database results greeting."""
    speeds = Speed.all()
    return render_template('')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
