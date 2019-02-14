import os
from flask import Flask

app = Flask(__name__)

# Import the blueprint
from personalwebsite.core.views import core

# Register
app.register_blueprint(core)
