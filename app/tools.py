import datetime

import os

from app import app, mail
from app.mod_account.models.Token import Token
from flask import flash
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
import requests


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(error, "error")


def generate_token(data):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(data, salt=app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        data = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    tk = Token.query.filter_by(token_value=token).first()
    if not tk or tk.used or tk.expires_on < datetime.datetime.now():
        return False
    return data


def send_email_mailgun(to_address, subject, html):
    try:
        r = requests. \
            post("https://api.mailgun.net/v2/%s/messages" % app.config['MAILGUN_DOMAIN'],
                 auth=("api", app.config['MAILGUN_KEY']),
                 data={
                     "from": app.config['MAIL_DEFAULT_SENDER'],
                     "to": to_address,
                     "subject": subject,
                     "html": html
                 }
                 )
        return True
    except Exception as e:
        flash(e, "error")
        return False


def send_email(to, subject, template):
    if os.environ.get('ENVIRONMENET', 'development') == 'production':
        return send_email_mailgun(to, subject, template)
    else:
        msg = Message(
            subject,
            recipients=[to],
            html=template,
            sender=app.config['MAIL_DEFAULT_SENDER']
        )
        try:
            mail.send(msg)
            return True
        except Exception as e:
            print e
            flash("Something went wrong and we couldn't send you an email! Please try again later.", "error")
        return False


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
