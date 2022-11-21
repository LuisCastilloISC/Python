from flask import Flask,request,jsonify
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from routes.user.user import appuser
from routes.images.images import imageUser
app = Flask(__name__)
app.register_blueprint(appuser)
app.register_blueprint(imageUser)
app.config.from_object(BaseConfig)

CORS(app)

bcrypt.init_app(app)
db.init_app(app)
#configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)






