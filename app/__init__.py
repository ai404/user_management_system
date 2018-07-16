from flask import Flask, render_template
from flask_images import Images
from flask_wtf import CSRFProtect
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import sys
import logging

# Define the WSGI application object
app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# Configurations
app.config.from_object('config.DevelopmentConfig')
# Enable csrf
csrf = CSRFProtect()
csrf.init_app(app)

images = Images(app)
# Define the database object which is imported
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Setup mail extension
mail = Mail(app)
from app.mod_account.models.Role import Role
from app.mod_account.models.User import User
from app.mod_account.models.Token import Token


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable
from app.mod_main.controllers import mod_main
from app.mod_account.controllers import mod_account

# Register blueprint(s)
app.register_blueprint(mod_main)
app.register_blueprint(mod_account)

db.create_all()

from template_filters import *
