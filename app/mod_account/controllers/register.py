from app import User
from app import db
from app.mod_account.controllers import mod_account
from app.mod_account.forms import RegisterForm
from app.mod_account.models.Profile import Profile
from flask import render_template, url_for, request
from flask_login import current_user, logout_user
from werkzeug.utils import redirect


@mod_account.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            u = User(form.email.data, form.password.data)

            db.session.add(u)
            db.session.commit()
            p = Profile(form.first_name.data, form.last_name.data, u.id)
            db.session.add(p)
            db.session.commit()
            u.send_confirmation()
            u.init_folders()
            logout_user()
            return redirect(url_for(".login"))
    return render_template("account/register_user.html", form=form)
