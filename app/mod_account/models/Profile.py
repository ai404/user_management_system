import os
from app import db
from flask import url_for


class Profile(db.Model):
    __tablename__ = 'profiles'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    picture = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship("User", back_populates="profile", uselist=False)

    def __init__(self, first_name, last_name, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    def get_picture(self):
        return self.picture if self.picture else "user.png"