from flask import Flask
from flask_cors import CORS
from app.routes import api

def create_app():
    app = Flask(__name__, static_folder='../', static_url_path='')
    CORS(app)

    app.register_blueprint(api, url_prefix="/api")

    @app.route('/')
    def home():
        return app.send_static_file('app.html')

    return app
