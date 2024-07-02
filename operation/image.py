from models.image import *
from utils.debug import DEBUG
from error_code import ErrorCode
from datetime import datetime

from db_config import db_init as db
from sqlalchemy import desc, func
import sys

class Image_opration():

    def _add(self,patient_id,file_info,file):
        DEBUG(func=f'{__name__} {self.__class__.__name__} {sys._getframe().f_code.co_name}')
        newimage=Images(Patient_ID=patient_id,Examine_Date=file_info['StudyDate'],
                        Image_Modality=file_info['ImageType'],Body_Part=file_info['BodyPart'],
                        Diagnosis_Notes=file_info['StudyDescription'],Image_data=file)
        #newimage=Images(Patient_ID='2024002624',Examine_Date=file_info['StudyDate'],
        #                Image_Modality='CT',Body_Part="unkown",
        #                Diagnosis_Notes="unkown",Image_data=file)
        ans,id = Model_add_image(newimage)
        DEBUG(add_image=ans)
        if ans != 0:
            return ErrorCode.IMAGES_ADD_ERROR,None
        return ans,id

    def _imagesall(self,patients_list):
        DEBUG(func=f'{__name__} {self.__class__.__name__} {sys._getframe().f_code.co_name}')
        #obatin all images of the patient according the patient_id;
        #images_list=Images.query.filter(Patient_ID=patient_id).order_by(Images.Examine_Date.desc()).all()
        patients_id=[patient.Patient_ID for patient in patients_list]
        images_list= Images.query.filter(Images.Patient_ID.in_(patients_id)).order_by(desc(Images.Examine_Date))
        DEBUG(queries_images_list=images_list)
        return images_list
    
image_opration = Image_opration()