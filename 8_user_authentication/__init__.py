
from decouple import config

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #? We use this __name__ argument to indicate the app's module or package -  so that Flask knows where to find other files, such as templates.
app.config.from_object(config("APP_SETTINGS")) #? You also set the config of the app using an environment variable called `APP_SETTINGS`

#? To use Flask-Bcrypt, Flask-SQLAlchemy, and Flask-Migrate in the app, you need to create the objects below.
Bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db) #? migrate the classes from each library respectively.

#* Registering Blueprints
  #? You'll need to register these blueprints, but we'll define them later.
from src.accounts.views import accounts_bp
from src.core.views import core_bp
