from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, TextAreaField, RadioField
from wtforms.validators import DataRequired, ValidationError
from models import User
from globalSettings import session


class LoginForm(FlaskForm):
    username = StringField(label='Enter username', validators=[DataRequired()])
    password = PasswordField(label='Enter password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class RegisterForm(FlaskForm):
    username = StringField(label='Enter username', validators=[DataRequired()])
    password = StringField(label='Enter password', validators=[DataRequired()])
    age = IntegerField(label='Enter your age')
    sex = StringField(label='Enter you sex')
    country = StringField(label='Enter your country')
    city = StringField(label='Enter your city')
    submit = SubmitField(label='Register')

    def validate_username(self, formUsername):
        user = session.query(User).filter(User.username==formUsername.data).first()

        if(formUsername.data == ''):
            raise ValidationError('Username can\'t be emty!')
        
        if(user):
            raise ValidationError('Username already exists! Please try a different username')

    def validate_password(self, formPassword):
        if(formPassword.data == ''):    
            raise ValidationError('Password can\'t be emty!')

class ProfileForm(FlaskForm):
    username = StringField(label='Enter username', validators=[DataRequired()])
    password = StringField(label='Enter password', validators=[DataRequired()])
    age = IntegerField(label='Enter your age')
    sex = StringField(label='Enter you sex')
    country = StringField(label='Enter your country')
    city = StringField(label='Enter your city')
    submit = SubmitField(label='Update')

    def validate_password(self, formPassword):
        if(formPassword.data == ''):    
            raise ValidationError('Password can\'t be emty!')

class DiaryLogForm(FlaskForm):
    name = StringField(label='Enter diary log name', validators=[DataRequired()])
    date = DateField(label='Diary log date', validators=[DataRequired()])
    log = TextAreaField(label='Enter you daily thoughts!', validators=[DataRequired()], render_kw={'cols': '30', 'rows': '10', 'placeholder': 'Write about your day :)'})
    visible = RadioField(label='Do you want this log to be visible?', choices=[('1','Yes'),('0','No')], default='1')
    submit = SubmitField(label='Confirm')

    def validate_name(self, formName):
        if(formName.data == ''):
            raise ValidationError('The name can\t be emty!')

    def validate_date(self, formDate):
        if(formDate.data == ''):
            raise ValidationError('The date can\'t be emty!')

    def validate_log(self, formLog):
        if(formLog.data == ''):
            raise ValidationError('The diary log can\'t be emty!')

        if(len(formLog.data) > 300):
            raise ValidationError('The diary log can have maximum 300 characters!')

