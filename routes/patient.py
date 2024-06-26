from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from utils.parse import parse_json_data
from error_code import ErrorCode
from flask import Blueprint,request
import hashlib,sys

patient = Blueprint('patient',__name__)

from api.patient import *

@patient.route('/query_all',methods=['GET'])
def query_all():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    ret_code,data = parse_json_data(request.data, ['doctor_id'])
    if ret_code != ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp

    # some check
    if data['doctor_id'] <= 0:
       resp = make_resp(ErrorCode.REQUEST_DATA_ERROR)
       return resp    

    ans,data=QueryAll(data['doctor_id'])
    resp = make_resp(ans,data)

    return resp
