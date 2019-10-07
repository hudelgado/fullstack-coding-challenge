import os

from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
  app = Flask(__name__)
  CORS(app)
  app_init(app, test_config)

  from translator.db import init_app_db
  init_app_db(app)

  from .api import api_bp
  from .client import client_bp
  app.register_blueprint(api_bp)
  app.register_blueprint(client_bp)

  return app

def app_init(app, test_config):
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE='sqlite:///%s' % os.path.join(app.instance_path, 'flaskr.sqlite'),
  )

  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)