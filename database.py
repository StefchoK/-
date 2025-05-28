from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

from flask_cors import CORS
CORS(app)

db = SQLAlchemy(app)
jwt = JWTManager(app)