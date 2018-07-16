import datetime
from app.mod_account.controllers import mod_account
from app import db
from app.mod_account.forms import ResetPasswordSubmit
from app.mod_account.models.User import User
from app.mod_account.models.Token import Token
from app.tools import confirm_token
from flask import request, flash, url_for, render_template, redirect
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash


@mod_account.route('/change/<token>', methods=['GET', 'POST'])
def change(token):
    verified_result = confirm_token(token)
    if token and verified_result:
        user = User.query.get(verified_result)
        password_submit_form = ResetPasswordSubmit(request.form)
        if request.method == "POST":
            if password_submit_form.validate():
                t = Token.query.filter_by(token_value=token).first()
                t.used = True

                user.password = generate_password_hash(password_submit_form.password.data)
                user.confirmed = True
                user.confirmed_on = datetime.datetime.now()
                db.session.add(user)
                db.session.add(t)
                db.session.commit()
                flash("Password updated successfully!", "info")
                return redirect(url_for('account.login'))
        return render_template("account/change_password.html", form=password_submit_form)
    else:
        flash("Invalid or Expired token", "error")
    return redirect(url_for("account.login"))


@mod_account.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    password_submit_form = ResetPasswordSubmit(request.form)
    if request.method == "POST":
        if password_submit_form.validate_on_submit():
            current_user.password = generate_password_hash(password_submit_form.password.data)
            db.session.add(current_user)
            db.session.commit()
            flash("Password updated successfully!", "info")
            return redirect(url_for('.edit'))
    return render_template("account/account.html", form=password_submit_form)
