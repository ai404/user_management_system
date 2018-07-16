from flask import Blueprint

mod_account = Blueprint('account', __name__, url_prefix='/account')

from login import *
from logout import *
from register import *
from confirm import *
from reset import *
from change import *
from profile import *
