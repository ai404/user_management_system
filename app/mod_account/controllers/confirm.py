import datetime

from app.mod_account.controllers import mod_account
from app import db, User
from app.mod_account.models.Token import Token
from app.tools import confirm_token
from flask import flash, url_for, redirect


@mod_account.route('/confirm/<token>')
def confirm_email(token):
    email = confirm_token(token)

    if not email:
        flash('Invalid or Expired Token!', 'error')
        return redirect(url_for('account.login'))
    user = User.query.filter_by(email=email).first()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'info')
    else:
        tk = Token.query.filter_by(token_value=token).first()
        tk.used = True

        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()

        db.session.add(tk)
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'info')
    return redirect(url_for('main.dashboard'))
