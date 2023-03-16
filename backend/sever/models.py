from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    password_hash = db.Column(db.String(128))
    subject_info = db.Column(db.String(500))
    # username, password_hash, permission
    class_id = db.Column(db.Integer)
    name = db.Column(db.String(10))
    permission = db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)