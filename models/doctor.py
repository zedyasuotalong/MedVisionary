

from db_config import db_init as db
# define doctor Model Class
class Doctors(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(64), unique=True, nullable=False,default='新用户')
    password = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Integer, nullable=True, default=0)
    age = db.Column(db.Integer, nullable=True, default=20)
    phone = db.Column(db.String(16), nullable=False, unique=True)
    email = db.Column(db.String(32), nullable=True, default='')
    level = db.Column(db.Integer, nullable=True, default=0)
    reg_time = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        # print('model')
        return f'<Doctor id:{self.id} account:{self.account}>'

def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except:
        ans = 1
    return ans

def Model_add_doctor(doctor):
    id = None
    try:
        db.session.add(doctor)
    except:
        return 1,None
    ans = Model_commit()
    id = doctor.id
    return ans,id

