from pydicom import dcmread
from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from utils.parse import form_to_data
from error_code import ErrorCode
from flask import Blueprint, jsonify,request
import hashlib,sys
import os
from utils.config import config

image = Blueprint('image',__name__)

from api.image import *

@image.route('/upload',methods=['GET','POST'])
def upload():
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    ret_code,data = form_to_data(request.data, ['patient_id','file'])
    if ret_code != ErrorCode.OK:
        resp = make_resp(ret_code)
        return resp 
    patient_id=data['patient_id']
    file = data['file']
    ans = Image_add(patient_id,file)
    DEBUG(ans=ans)
    resp,data = make_resp(ans)
    return resp,data