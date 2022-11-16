from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class RegistrationForm(FlaskForm):
    Username= StringField('Username', 
                        validators=[DataRequired(),Length (min=2, max=20)])
    Email=StringField('Email',
                  validators=[DataRequired(), Email()])
    Password=PasswordField('Password', validators=[DataRequired()])
    confirm_Password=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    submit=SubmitField('Sign up')

class LoginForm(FlaskForm):
    Email=StringField('Email',
                  validators=[DataRequired(), Email()])
    Password=PasswordField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Login')