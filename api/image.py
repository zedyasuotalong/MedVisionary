from datetime import datetime
from io import BytesIO
import time
import random
import threading
import time

import pydicom

from operation.image import image_opration
from utils.data_process import Class_To_Data
from utils.debug import DEBUG
from error_code import ErrorCode
# from utils.verify_code import send_code
import hashlib,sys

def parse_dicom_datetime(date_str, time_str):
    """ 将 DICOM 日期和时间格式转换为 datetime 对象 """
    try:
        dicom_datetime_str = date_str + time_str.split('.')[0]
        return datetime.strptime(dicom_datetime_str, '%Y%m%d%H%M%S')
    except ValueError:
        return None

def Image_add(patient_id,file):
    DEBUG(func=f'{__name__} {sys._getframe().f_code.co_name}')
    #obatin the received file
    file_content = file.read()
    dicom_data = pydicom.dcmread(BytesIO(file_content))

    #parse the datetime of the image
    study_date = dicom_data.get((0x0008, 0x0020), '').value if dicom_data.get((0x0008, 0x0020)) else ''
    study_time = dicom_data.get((0x0008, 0x0030), '').value if dicom_data.get((0x0008, 0x0030)) else ''
    study_datetime = parse_dicom_datetime(study_date, study_time)
    
    #parse other information of the image
    image_info={
        'PatientName': str(dicom_data.get((0x0010, 0x0010), 'Unknown').value if dicom_data.get((0x0010, 0x0010)) else 'Unknown'),
        'PatientID': str(dicom_data.get((0x0010, 0x0020),  'Unknown').value if dicom_data.get((0x0010, 0x0020)) else 'Unknown'),
        'BirthDate': dicom_data.get((0x0010, 0x0030), 'Unknown').value if dicom_data.get((0x0010, 0x0030)) else 'Unknown',
        'PatientSex': str(dicom_data.get((0x0010, 0x0040), 'Unknown').value if dicom_data.get((0x0010, 0x0040)) else 'Unknown'),
        'StudyDate': study_datetime,
        'StudyDescription': str(dicom_data.get((0x0008, 0x1030),'Unknown').value if dicom_data.get((0x0008, 0x1030)) else 'Unknown'),
        'BodyPart': str(dicom_data.get((0x0008,0x0015),'Unknown').value if dicom_data.get((0x0008, 0x0015)) else 'Unknown'),
        'ImageType': dicom_data.get((0x0008, 0x0061), 'Unknown').value if dicom_data.get((0x0008, 0x0061)) else 'Unknown'
    }
    #print(image_info)
    ans = image_opration._add(patient_id,image_info,dicom_data)
    DEBUG(ans=ans)
    return ans