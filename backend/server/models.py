from .extentions import db
from werkzeug.security import generate_password_hash, check_password_hash


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer)
    subject_name = db.Column(db.String(50), unique=True)
    teacher_info = db.Column(db.String(500))
    teacher_name = db.Column(db.String(10))
    subject_info = db.Column(db.String(500))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __init__(self, role, subject_name, teacher_info,teacher_name, subject_info, username, pwd):
        self.username = username
        self.role = role
        self.subject_name = subject_name
        self.teacher_name = teacher_name
        self.teacher_info = teacher_info
        self.subject_info = subject_info
        self.set_password(pwd)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return  "{}{}{}{}".format(self.username,self.password_hash,self.subject_name,self.subject_info)