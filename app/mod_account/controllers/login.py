from app import app
from app.mod_account.controllers import mod_account
from app.mod_account.forms import LoginForm
from app.mod_account.models.User import User
from flask import render_template, request, flash, url_for, redirect
from flask_login import login_user, LoginManager, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "account.login"


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@mod_account.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = LoginForm(request.form)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        u = User.authenticate(email, password)
        if form.validate():
            if u:
                if not u.confirmed:
                    flash("This email is not verified. Please check your Inbox", "error")
                else:
                    remember_me = False
                    if 'remember_me' in request.form:
                        remember_me = True
                    login_user(u, remember=remember_me)
                    return redirect(request.args.get("next") if request.args.get("next") else url_for("main.dashboard"))
            else:
                flash("Username/Password doesn't match", "error")
    return render_template("account/login_user.html", form=form)

