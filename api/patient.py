import time
import random
import threading
import time

from operation.patient import patient_opration
from utils.data_process import Class_To_Data
from utils.debug import DEBUG
from error_code import ErrorCode
# from utils.verify_code import send_code
import hashlib,sys

def QueryAll(doctor_id):
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    #根据医生ID查询对应之下的所有患者信息；【患者ID、患者姓名、性别、出生日期、联系方式】
    patients_list = patient_opration._doctorall(doctor_id)
    patients_list = Class_To_Data(patients_list, 
                    ['Patient_ID', 'Patient_Name', 'Examine_Date', 'Diagnosis_Notes', 'Device', 'Number_of_images'], 0)
    DEBUG(patients_list=patients_list)
    return ErrorCode.OK,patients_list

