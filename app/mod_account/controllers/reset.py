from app.mod_account.controllers import mod_account
from app import User
from app.mod_account.forms import ResetPassword
from flask import request, render_template


@mod_account.route('/reset', methods=('GET', 'POST',))
def reset():
    form = ResetPassword(request.form)  # form
    if request.method == "POST":
        if form.validate():
            email = form.email.data
            user = User.query.filter_by(email=email).first()
            if user:
                user.send_reset_link()
                form=ResetPassword()
    return render_template('account/forgot_password.html', form=form)
