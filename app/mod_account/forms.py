from app.mod_account.models.User import User
from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, PasswordField, validators, FileField


class ExistingUser(object):
    def __init__(self, message="Email doesn't exists"):
        self.message = message

    def __call__(self, form, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(self.message)


email_rules = [validators.DataRequired(),
               validators.Email("Enter a valid Email"),
               ExistingUser(message='Email address is not available')
               ]

password_rules = [
    validators.DataRequired(),
    validators.length(min=5, message="Minimum length is 5 chars"),
    validators.EqualTo('password_confirm', message='Passwords must match')
]


class ResetPassword(FlaskForm):
    email = StringField('Email', validators=[validators.DataRequired(),
                                             validators.Email("Enter a valid Email")],
                        description="Enter your register email address")


class ResetPasswordSubmit(FlaskForm):
    password = PasswordField('New Password', validators=password_rules)
    password_confirm = PasswordField('Confirm Password', validators=[validators.DataRequired()], description="Re-enter Password")


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[validators.DataRequired()])
    last_name = StringField('Last Name', validators=[validators.DataRequired()])
    email = StringField('Email', validators=email_rules)
    password = PasswordField('Password', validators=password_rules)
    password_confirm = PasswordField('Repeat Password', validators=[validators.DataRequired()], description="Re-enter Password")


class UploadPhotoForm(FlaskForm):
    picture = FileField('Select a valid photo')


class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[validators.DataRequired()])
    last_name = StringField('Last Name', validators=[validators.DataRequired()])
    phone = StringField('Phone', validators=[validators.regexp("^$|^(\d){5,20}$", message="Please enter a valid phone number")])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.DataRequired(),
                                             validators.Email("Enter a valid Email")])
    password = PasswordField('Password', validators=[validators.DataRequired()])
