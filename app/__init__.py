from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET KEY'] = "my-totally-random-secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wfmbtzdmojfapi:e060475cbbe70fb9a0393b9e39becb0be9fe08d3afdbd33a4a8566b9799de939@ec2-3-230-238-86.compute-1.amazonaws.com:5432/d1utr9l2rhd7pc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config.from_object(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
