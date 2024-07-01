from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from utils.parse import parse_json_data
from error_code import ErrorCode
from flask import Blueprint,request
import hashlib,sys

patient = Blueprint('patient',__name__)

from api.patient import *

@patient.route('/query_by_doctor_id',methods=['GET'])
def query_by_doctor_id():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    ret_code,data = parse_json_data(request.data, ['doctor_id'])
    if ret_code != ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp

    # some check
    if data['doctor_id'] <= 0:
       resp = make_resp(ErrorCode.REQUEST_DATA_ERROR)
       return resp    

    ans,data=QueryByDoctorID(data['doctor_id'])
    resp = make_resp(ans,data)

    return resp

@patient.route('/query_by_patient_id',methods=['GET'])
def query_by_patient_id():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    ret_code,data = parse_json_data(request.data, ['patient_id'])
    if ret_code != ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp

    # some check
    if data['patient_id'] <= 0:
       resp = make_resp(ErrorCode.REQUEST_DATA_ERROR)
       return resp

    ans,data=QueryByPatientID(data['patient_id'])
    resp = make_resp(ans,data)

    return resp

@patient.route('/query_by_patient_name',methods=['GET'])
def query_by_patient_name():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    ret_code,data = parse_json_data(request.data, ['patient_name'])
    if ret_code != ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp

    # some check
    if data['patient_name'] is None or len(data['patient_name']) == 0:
       resp = make_resp(ErrorCode.REQUEST_DATA_ERROR)
       return resp

    ans,data=QueryByPatientName(data['patient_name'])
    resp = make_resp(ans,data)

    return resp

@patient.route('/query_default_num',methods=['GET'])
def query_default_num():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    # ret_code,data = parse_json_data(request.data, ['number'])
    # if ret_code != ErrorCode.OK:
    #     resp = make_resp(ret_code)
    #     return resp

    # # some check
    # if data['number'] <= 0:
    #    resp = make_resp(ErrorCode.REQUEST_DATA_ERROR)
    #    return resp

    # ans,data=QueryLimitNum(data['number'])
    ans,data=QueryLimitNum(15)
    resp = make_resp(ans,data)

    return resp
