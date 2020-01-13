from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.create_all()

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

