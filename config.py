import os
DEBUG = True

SECRET_KEY = os.urandom(24)

# hide warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'comp208'

# Configuration variables for the database
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'serendipity'
USERNAME = 'root'
PASSWORD = 'SXc2002627SXc'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


CMS_USER_ID = 'ASDNJFKMML'