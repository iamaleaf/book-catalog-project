from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# initialise Flask app
app = Flask(__name__)
# read and apply config file
app.config.from_object(Config)
# initialise database
db = SQLAlchemy(app)

# Imports added at the bottom to avoid circular imports
from app import routes, models  # noqa: F401
# from app import models
# db.create_all()
