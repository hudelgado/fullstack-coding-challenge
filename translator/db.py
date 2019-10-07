from flask.cli import with_appcontext
from playhouse.flask_utils import FlaskDB
import click, os

db_wrapper = FlaskDB()

from .models import Translation

def init_app_db(app):
  """Initialize a new application
  
  Does the following task:
    - Creates the data folder
    - Initialize the database
    - Register close_db on teardown
    - Register the cli commands
  """

  init_db_folder(app.instance_path)
  db_wrapper.init_app(app)
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)

def init_db_folder(folder):
  """Initialize database folder
  
  Create the folder to store the database
  if it didn't exist yet
  """

  try:
    os.makedirs(folder)
  except OSError:
    pass

def get_db():
  """Retrieve the current database"""

  return db_wrapper.database

def close_db(e=None):
  """Closes the database"""
  
  get_db().close()

def init_db():
  """Initialize the database

  Create the tables in the database
  """

  get_db().create_tables([Translation])

@click.command('init-db')
@with_appcontext
def init_db_command():
  """Create new tables"""
  init_db()
  click.echo('Initialized the database.')
