import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in ANY OS we find ourselves in,
# and allow outside files/folders to be added to the project
# from the base directory.

load_dotenv(os.path.join(basedir, '.env'))



class Config():
    """
    Set configuration variables for the flask app.
    Using Environment variables where available,
    otherwise create the config variable if not 
    done already.
    """

    # REMEMBER TO GITIGNORE VARY LARGE FILES and SENSITIVE INFO
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # this turns off messages from sqlalchemy regarding updates to our db,
                                          # otherwise gets really cluttered