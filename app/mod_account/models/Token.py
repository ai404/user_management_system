import datetime

from app import db
from sqlalchemy import func
from sqlalchemy.sql import expression


class Token(db.Model):
    __tablename__ = 'tokens'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token_value = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    expires_on = db.Column(db.DateTime, default=lambda x: datetime.datetime.now() + datetime.timedelta(minutes=60))
    used = db.Column(db.Boolean,server_default=expression.false())

    def __init__(self, user_id, token):
        self.token_value = token
        self.user_id = user_id
