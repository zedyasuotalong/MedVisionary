from models.doctor import *
from utils.debug import DEBUG
from error_code import ErrorCode
from datetime import datetime

from db_config import db_init as db
from sqlalchemy import func
import sys

class Doctor_opration():
    def __init__(self):
        # DEBUG(func='Doctor_opration/__init__')
        self.__fields__ = ['Doctor_ID','account','password','gender','age','phone','email','level','reg_time'] 

    def _all(self):
        DEBUG(func=f'{__name__} {self.__class__.__name__} {sys._getframe().f_code.co_name}')
        doctor_list = Doctors.query.all()
        DEBUG(doctor_list=doctor_list)
        return doctor_list
    
    def _info(self, Doctor_ID):
        DEBUG(func=f'{__name__} {self.__class__.__name__} {sys._getframe().f_code.co_name}')
        doctor_list = Doctors.query.filter_by(Doctor_ID=Doctor_ID).first()
        DEBUG(doctor_list=doctor_list)
        return doctor_list
    
    def _login(self, account):
        DEBUG(func=f'{__name__} {self.__class__.__name__} {sys._getframe().f_code.co_name}')
        doctor_list = Doctors.query.filter_by(account=account).first()
        DEBUG(doctor_list=doctor_list)

        return doctor_list
    
    def _update(self, Doctor_ID, dict_value):
        DEBUG(func=f'{__name__} {self.__class__.__name__} {sys._getframe().f_code.co_name}')
        data = Doctors.query.filter_by(Doctor_ID=Doctor_ID)
        if data.first() is None:
            return ErrorCode.DOCTOR_ACCOUNT_NONEXISTS
        try:
            ans = data.update(dict_value) # ans should be 1
        except:
            ans = 0
        DEBUG(update_ans=ans)
        if ans != 1:
            return ErrorCode.CHANGE_DOCTOR_INFO_ERROR

        ans = Model_commit()
        DEBUG(commit_ans=ans)
        if ans != 0:
            return ErrorCode.CHANGE_DOCTOR_INFO_ERROR
        return ans

doctor_opration = Doctor_opration()