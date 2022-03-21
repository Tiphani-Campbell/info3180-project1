from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "my-totally-random-secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bqhaqhykbajcii:020cb17e6784c2d259a5fae71f197808c6a631c1aeab23cd29fcb685c2352d14@ec2-34-224-226-38.compute-1.amazonaws.com:5432/dbvda02i2cs6q6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config.from_object(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
