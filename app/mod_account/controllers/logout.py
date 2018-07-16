from app.mod_account.controllers import mod_account
from flask import flash,redirect, url_for
from flask_login import login_required, logout_user


@mod_account.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for(".login"))



