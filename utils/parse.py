import json
from flask import request

from utils.debug import INFO
from error_code import ErrorCode


def parse_json_data(data, params):
    try:
        data = json.loads(request.data) # data is json
    except: # data is not json
        print()
        return ErrorCode.REQUEST_DATA_FORMAT_ERROR,None
    INFO(request_data=data)
    for key in params:
        if key not in data:
            return ErrorCode.MISSING_REQUIRED_PARAMS,None
    return ErrorCode.OK,data
