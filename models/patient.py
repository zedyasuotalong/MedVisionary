from db_config import db_init as db

class Patients(db.Model):
    __tablename__ = "patients"
    Patient_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Patient_Name = db.Column(db.String(100), nullable=False)
    Sex=db.Column(db.String(2),nullable=False)
    Birth_Date=db.Column(db.Date,nullable=False)
    Phone=db.Column(db.String(11),nullable=True)

    def __repr__(self):
        # print('model')
        return f'<Patient id:{self.Patient_ID} Patient Name:{self.Patient_Name}>'
    

def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except:
        ans = 1
    return ans

def Model_add_patient(patient):
    id = None
    try:
        db.session.add(patient)
    except:
        return 1,None
    ans = Model_commit()
    id = patient.Patient_ID
    return ans,id


