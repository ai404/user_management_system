from app.mod_main.controllers import mod_main
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_login import login_required


@mod_main.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("main/dashboard.html")
