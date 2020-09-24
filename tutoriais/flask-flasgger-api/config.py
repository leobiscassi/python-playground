from flask import Flask
from flask_cors import CORS
from app import api_bp
from cassandra.auth import PlainTextAuthProvider
from flasgger import Swagger

flask_app = Flask(__name__)
CORS(flask_app)
flask_app.config['SWAGGER'] = {"title" : "People API",
                               "uiversion" : 2}
swagger = Swagger(flask_app)

flask_app.register_blueprint(api_bp, url_prefix="/api")

auth = PlainTextAuthProvider(username="cassandra", password="")