import datetime

import os
from app import db
from app.mod_account.models.AccountStatus import AccountStatus
from app.mod_account.models.Profile import Profile
from app.mod_account.models.Role import Role
from app.mod_account.models.Token import Token
from app.mod_account.models.SubscriptionPlan import SubscriptionPlan

from app.tools import generate_token, send_email
from flask import url_for, render_template, flash
from sqlalchemy.sql import expression
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # first_name = db.Column(db.String(200), nullable=False)
    # last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    account_status_id = db.Column(db.ForeignKey(AccountStatus.id, ondelete='CASCADE'), server_default=db.text("'1'"))
    role_id = db.Column(db.ForeignKey('roles.id', ondelete='CASCADE'), server_default=db.text("'1'"))
    subscription_id = db.Column(db.ForeignKey(SubscriptionPlan.id, ondelete='CASCADE'), server_default=db.text("'1'"))
    last_login = db.Column(db.DateTime)
    confirmed = db.Column(db.Boolean, server_default=expression.false())
    confirmed_on = db.Column(db.DateTime)
    aggrement_accepted = db.Column(db.Boolean, server_default=expression.false())

    account_status = db.relationship(AccountStatus, backref="account_status")
    role = db.relationship(Role, backref="roles")
    subscription = db.relationship("SubscriptionPlan", backref="subscription_plans")
    profile = db.relationship(Profile, backref="profiles", uselist=False, passive_deletes='all')

    def __init__(self, email, password, confirmed=False):
        # self.first_name = first_name
        # self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)
        self.confirmed = confirmed
        if confirmed:
            self.confirmed_on = datetime.datetime.now()

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def init_folders(self):
        try:
            os.makedirs("media/users/{id}/pictures".format(id=self.id))
        except:
            pass

    def send_confirmation(self):
        token = generate_token(self.email)
        confirm_url = url_for('.confirm_email', token=token, _external=True)
        html = render_template('account/emails/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        if send_email(self.email, subject, html):
            flash("A confirmation email has been sent via email.", "info")

        t = Token(self.id, token)
        db.session.add(t)
        db.session.commit()

    def send_reset_link(self):
        token = generate_token(self.id)
        reset_url = url_for('.change', token=token, _external=True)
        html = render_template('account/emails/reset.html', reset_url=reset_url)
        subject = "Password Reset Request"
        if send_email(self.email, subject, html):
            flash("An email has been sent. Check your Inbox.", "info")

        t = Token(self.id, token)
        db.session.add(t)
        db.session.commit()

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter_by(email=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return None

    @classmethod
    def identity(cls, payload):
        return User.query.filter(User.id == payload['identity']).scalar()

    def __repr__(self):
        return '<User %r>' % self.id
