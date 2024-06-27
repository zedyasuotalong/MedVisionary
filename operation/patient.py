from flask import jsonify
from models.patient import *
from models.doctorpatient import *
from models.image import *
from utils.debug import DEBUG
from error_code import ErrorCode
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

from db_config import db_init as db
from sqlalchemy import desc, func
import sys

class Patient_opration():
    def __init__(self):
        # DEBUG(func='Doctor_opration/__init__')
        self.__fields__ = ['Patient_ID','Patient_Name','Sex','gender','Birth_Date','phone'] 

    #query all patients in the database;
    def _all(self):
        DEBUG(func=f'{__name__} {self.__class__.__name__} {sys._getframe().f_code.co_name}')
        patient_list=Patients.query.all()
        DEBUG(patient_list=patient_list)
        return patient_list

    #query all patients with the same doctor ID
    def _doctorall(self,doctor_id):
        DEBUG(func=f'{__name__} {self.__class__.__name__} {sys._getframe().f_code.co_name}')
        #obatin all patients id belong to the doctor id
        patients_list=(db.session.query(Patients.Patient_ID, Patients.Patient_Name, Images.Examine_Date,Images.Diagnosis_Notes,
                                        Images.Device,Images.Number_of_images)
                             .join(DoctorPatient, Patients.Patient_ID == DoctorPatient.Patient_ID)
                             .filter(DoctorPatient.Doctor_ID == doctor_id)
                             .join(Images, Patients.Patient_ID == Images.Patient_ID)
                             .all())
        DEBUG(patients_list=patients_list)
        return patients_list

patient_opration = Patient_opration()