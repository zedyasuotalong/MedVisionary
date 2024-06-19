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

app.register_blueprint(doctor, url_prefix="/doctor")

@app.route('/')
def ping():
    return "ok"

if __name__ == '__main__':
    # context = ('ssl_cert/server.crt', 'ssl_cert/server.key')
    # app.run(host='0.0.0.0',port=5000,debug=True, ssl_context=context)
    app.run(host=config['server_ip'],port=config['server_port'],debug=True)
