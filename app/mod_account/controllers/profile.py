import os
from app import db
from app.mod_account.controllers import mod_account
from app.mod_account.forms import UploadPhotoForm, ProfileForm
from flask import render_template, request, flash, url_for, redirect, jsonify
from flask_login import login_required, current_user
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename


@mod_account.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    p = current_user.profile

    photo_form = UploadPhotoForm()
    form = ProfileForm(request.form)

    if request.method == "POST":
        if form.validate():
            form.populate_obj(p)
            db.session.add(p)
            db.session.commit()
            flash("Profile updated successfully!", 'info')
    else:
        form = ProfileForm(obj=p)
    return render_template("account/profile.html", photo_form=photo_form, form=form)


@mod_account.route('/profile/picture/update', methods=['POST'])
@login_required
def picture_update():
    photo_form = UploadPhotoForm(CombinedMultiDict((request.files, request.form)))
    if photo_form.validate():
        fileext = secure_filename(photo_form.picture.data.filename).split(".")[-1]
        filename = 'users/%d/pictures/%d.' % (current_user.id, current_user.id) + fileext
        photo_form.picture.data.save("media/"+filename)

        p = current_user.profile
        p.picture = os.path.normpath(filename)
        db.session.add(p)
        db.session.commit()
        flash("Picture updated successfully","info")

    else:
        print photo_form.errors
        flash("Something went wrong! your account picture couldn't be updated","error")
    return jsonify(success=True)
