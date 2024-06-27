from db_config import db_init as db
import datetime
# define doctor Model Class
class Images(db.Model):
    __tablename__ = 'images'
    Image_ID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Examine_Date = db.Column(db.DateTime, default=datetime.datetime.now,nullable=False)
    Image_Modality = db.Column(db.String(10),nullable=False)
    Body_Part=db.Column(db.String(20))
    Patient_ID=db.Column(db.String(50),db.ForeignKey('patients.Patient_ID'), nullable=False)
    Diagnosis_Notes=db.Column(db.Text)
    Image_data = db.Column(db.LargeBinary,nullable=False)
    Device = db.Column(db.String(64), nullable=False)
    Number_of_images = db.Column(db.Integer, nullable=False)


def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        ans = 1
    return ans

def Model_add_image(image):
    id = None
    try:
        db.session.add(image)
    except:
        return 1,None
    ans = Model_commit()
    id = image.Image_ID
    return ans,id



