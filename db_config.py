
from flask_sqlalchemy  import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from utils.config import config

static_folder = 'static'
app = Flask(__name__, static_folder=static_folder, static_url_path='/')
CORS(app, supports_credentials=True)
# 数据库配置                                               用户名：密码@ip：port/数据库名字
app.config['SQLALCHEMY_DATABASE_URI'] = \
  'mysql+pymysql://{}:{}@{}:{}/{}'.\
    format(config['db_username'],config['db_password'],config['db_ip'],config['db_port'],config['db_database'])

# 数据库操作对象
db_init = SQLAlchemy(app)

