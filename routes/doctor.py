from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from utils.parse import parse_json_data
from error_code import ErrorCode
from flask import Blueprint,request
import hashlib,sys

doctor = Blueprint('doctor',__name__)

from api.doctor import *

@doctor.route('/login',methods=['POST'])
def login():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    # 键'password'对应的值是密码或者验证码
    # login_type==0，password里存的是密码
    # login_type==1，password里存的是验证码 #TODO
    ret_code,data = parse_json_data(request.data, ['login_type', 'account', 'password'])
    if ret_code != ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp

    # some check
    if data['login_type'] not in [0,1]:
        resp = make_resp(ErrorCode.UNSUPPORTED_LOGIN_TYPE)
        return resp    

    login_type = data['login_type']
    account   = data['account']
    password  = data['password']
    
    ans,data = Doctor_login(login_type, account, password)
    resp = make_resp(ans,data)

    return resp

@doctor.route('/send_verify_code',methods=['POST'])
def send_verify_code():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    # TODO

    return None

@doctor.route('/verify_verify_code',methods=['POST'])
def verify_verify_code():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    # TODO

    return None

@doctor.route('/change_sensitive_info',methods=['POST'])
def change_sensitive_info():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    # type==0，value里存的是电话号码
    # type==1，value里存的是密码
    ret_code,data = parse_json_data(request.data, ['id', 'type', 'value'])
    if ret_code!= ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']
    type = data['type']
    value = data['value']

    if type not in [0,1]:
        resp = make_resp(ErrorCode.UNSUPPORTED_DOCTOR_CHANGE_INFO_TYPE)
        return resp
    if value is None:
        return make_resp(ErrorCode.REQUEST_DATA_ERROR)
        
    data = dict()
    if type == 0:
        data['phone'] = value    
    else:
        data['password'] = hashlib.sha1(value.encode('utf-8')).hexdigest()

    ans = Doctor_change_info(id, data)
    resp = make_resp(ans)

    return resp

@doctor.route('/change_info',methods=['POST'])
def change_info():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    # 除了id，其他值可以为空
    ret_code,data = parse_json_data(request.data, ['id', 'name', 'email', 'age', 'gender',])

    if ret_code!= ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']
    data.pop('id')
    print(data)

    ans = Doctor_change_info(id, data)
    resp = make_resp(ans)

    return resp

@doctor.route('/info',methods=['GET','POST'])
def info():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    ret_code,data = parse_json_data(request.data, ['id'])

    if ret_code!= ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp

    ans,data = Doctor_info(data['id'])
    DEBUG(ans=ans)
    DEBUG(data=data)
    resp = make_resp(ans,data)

    return resp
