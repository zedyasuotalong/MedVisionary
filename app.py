import time
from flask import Flask,request
import json


import sys
import datetime
# app = Flask(__name__)
from db_config import app
from utils.debug import Logger
from utils.config import config

sys.stdout = Logger(config['log_path'], sys.stdout)
print('Server Begins...{}'.format(datetime.datetime.now()))

# doctor模块
from routes.doctor import doctor
from routes.patient import patient

#register_blueprint 用于注册一个 Blueprint 对象，以组织和管理路由和视图函数，使代码更加模块化;flask应用app中注册医生视图；
app.register_blueprint(doctor, url_prefix="/doctor")
app.register_blueprint(patient,url_prefix="/patient")

@app.route('/')
def ping():
    return "ok"

if __name__ == '__main__':
    # context = ('ssl_cert/server.crt', 'ssl_cert/server.key')
    # app.run(host='0.0.0.0',port=5000,debug=True, ssl_context=context)
    app.run(host=config['server_ip'],port=config['server_port'],debug=True)
