import os
from bottle import run, TEMPLATE_PATH

from backend.handlers import app
from backend.static_handlers import staticHandler
from backend.page_handlers import pageHandler

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))

app.merge(staticHandler)
app.merge(pageHandler)
run(app, host='localhost', port=os.environ.get('PORT', 5000))