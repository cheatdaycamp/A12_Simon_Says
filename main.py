import os
from bottle import run, TEMPLATE_PATH

# importing modules
from backend.handlers import app
from backend.static_handlers import staticHandler
from backend.page_handlers import pageHandler

# Specifying the template path:
TEMPLATE_PATH.insert(0, os.path.dirname(__file__))

# Merging the game handlers:
app.merge(staticHandler)
app.merge(pageHandler)

# Setting the server:
if os.environ.get('APP_LOCATION') == 'heroku':
    run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(app, host='localhost', port=os.environ.get('PORT', 5000))

