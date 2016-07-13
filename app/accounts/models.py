import datetime

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True, nullable=False)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    password_hash = db.Column(db.String(255), index=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    def __init__(self, username, email, password, first_name=None, last_name=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password field is not readable attribute.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def fullname(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __repr__(self):
        return "<User: %r>" % self.email
