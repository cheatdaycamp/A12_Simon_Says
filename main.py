import os
from bottle import run, TEMPLATE_PATH, debug

from backend.handlers import app
from backend.static_handlers import staticHandler
from backend.page_handlers import pageHandler
from sys import argv

DEBUG = os.environ.get("DEBUG")
debug(True)

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))

app.merge(staticHandler)
app.merge(pageHandler)

run(app, host='localhost', port=os.environ.get('PORT', 5000))

if DEBUG:
    run(app, host='localhost', port=os.environ.get('PORT', 5000))
else:
    run(app, host='0.0.0.0', port=argv[1])