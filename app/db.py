import os

from flask import Flask

from models import db

FLASK_RESPONSE = "Flask is running"
HOST = os.environ.get("MYSQL_HOST", "mysql")
USER = os.environ.get("MYSQL_USER", "root")
PASSWORD = os.environ.get("MYSQL_PASSWORD", "password")
DB_NAME = os.environ.get("DB_NAME, user_auth")

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:3306/user_auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
