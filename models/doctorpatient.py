from db_config import db_init as db

class DoctorPatient(db.Model):
    __tablename__ = "doctorpatient"
    Relation_ID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Doctor_ID = db.Column(db.Integer, db.ForeignKey('doctor.Doctor_ID'), nullable=False)
    Patient_ID = db.Column(db.Integer, db.ForeignKey('doctor.Patient_ID'), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('Doctor_ID', 'Patient_ID', name='unique_doctor_patient'),
    )

    #def __repr__(self):
        # print('model')
        #return f'<Patient id:{self.Patient_ID} Patient Name:{self.Patient_Name}>'
    

def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except:
        ans = 1
    return ans

def Model_add_doctorpatient(doctorpatient):
    id = None
    try:
        db.session.add(doctorpatient)
    except:
        return 1,None
    ans = Model_commit()
    id = doctorpatient.Relation_ID
    return ans,id