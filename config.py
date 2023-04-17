import os
DEBUG = True

SECRET_KEY = os.urandom(24)

# hide warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SECRET_KEY = 'comp208'

# Configuration variables for the database
#  127.0.0.1 47.243.187.169
HOSTNAME = '127.0.0.1' 
PORT     = '3306' # 3306
DATABASE = 'serendipity'
USERNAME = 'root'
PASSWORD = 'SXc2002627SXc'  
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


CMS_USER_ID = 'ASDNJFKMML'
FRONT_USER_ID = 'ASKNDLLSM'


MAIL_SERVER = "smtp.gmail.com"
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_PORT = 587
MAIL_USERNAME = "xinchi.shi20@gmail.com"
MAIL_PASSWORD = "smzewsthweshmacs"
MAIL_DEFAULT_SENDER = "xinchi.shi20@gmail.com"

# Configuration for flask-paginate
PER_PAGE = 2