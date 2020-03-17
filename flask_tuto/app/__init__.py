from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app01 = Flask(__name__)
app01.config.from_object(Config)
db = SQLAlchemy(app01)
migrate = Migrate(app01, db)

from app import routes, models
