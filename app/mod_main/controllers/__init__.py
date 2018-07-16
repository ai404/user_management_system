from flask import Blueprint

mod_main = Blueprint('main', __name__, url_prefix='/')

from dashboard import *
