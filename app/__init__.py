from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:password@dbserver/heroquest'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
csrf = CSRFProtect(app)

from app import routes, models
