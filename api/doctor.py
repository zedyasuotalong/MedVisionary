import time
import random
import threading
import time

from operation.doctor import doctor_opration
from utils.data_process import Class_To_Data
from utils.debug import DEBUG
from error_code import ErrorCode
# from utils.verify_code import send_code
import hashlib,sys

def Doctor_login(login_type,account,pwd):
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')

    data = doctor_opration._login(account)
    if data is None:
        return ErrorCode.DOCTOR_ACCOUNT_NONEXISTS,None
    data = Class_To_Data(data, doctor_opration.__fields__, 1)
    if len(data) == 0:
        return ErrorCode.DOCTOR_ACCOUNT_NONEXISTS,None
    id = dict()
    id['doctor_id'] = data['Doctor_ID']

    # 手机号，验证码登录
    if login_type == 1:
        # TODO
        pass
    
    # 账号，密码登录
    if data['password'] is None:
        return ErrorCode.DOCTOR_PASSWORD_NOTSET,None
    pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
    if pwd != data['password']:
        return ErrorCode.DOCTOR_PASSWORD_ERROR,None
    
    return ErrorCode.OK,id

def Doctor_send_verify_code(type, phone):
    #TODO
    pass

def Doctor_verify_verify_code(phone, verify_code):
    #TODO
    pass

def Doctor_change_info(id, dict_value):
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    ans = doctor_opration._update(id, dict_value)
    return ans

def Doctor_info(id,):
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    data = doctor_opration._info(id)
    if data is None:
        return ErrorCode.DOCTOR_ACCOUNT_NONEXISTS,None
    
    data = Class_To_Data(data,doctor_opration.__fields__, 1)
    DEBUG(data=data)
    if len(data) == 0:
        return ErrorCode.DOCTOR_ACCOUNT_NONEXISTS,None
    return ErrorCode.OK,data
