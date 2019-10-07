from flask import (Blueprint, send_from_directory)
import os

client_bp = Blueprint('client', __name__, url_prefix='/', static_folder="../www")

@client_bp.route('/main.js')
def app_bundle():
  return client_bp.send_static_file('main.js')

@client_bp.route('/css/<file>')
def css_files(file):
  return send_from_directory(os.path.join(client_bp.static_folder, 'css'), file)

@client_bp.route('/font/<base>/<file>')
def font_files(base, file):
  print(base, file)
  return send_from_directory(os.path.join(client_bp.static_folder, 'font', base), file)

@client_bp.route('/')
def root(path=None):
  return client_bp.send_static_file('index.html')
