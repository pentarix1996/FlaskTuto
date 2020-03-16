from flask import Flask
from config import Config

app01 = Flask(__name__)
app01.config.from_object(Config)

from app import routes
