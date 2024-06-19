from flask import make_response
import json
from error_code import ErrorCode
from utils.debug import *

def make_resp(code : int, resp_data=None):
  data = dict()
  data['status'] = code
  data['msg'] = ErrorCode.get_description(code)
  if (resp_data is not None) and (code == 0):
    data['data'] = resp_data
  if code != 0:
    ERROR(error_code=code, error_msg=ErrorCode.get_description(code))
  else: 
    INFO(response_data=data)
  resp = make_response(json.dumps(data, ensure_ascii=True))
  resp.headers['Content-Type'] = 'application/json'
  return resp