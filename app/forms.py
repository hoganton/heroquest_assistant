from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')


class HeroForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    character = StringField('Character', validators=[DataRequired()])
    attack_dice = IntegerField('Attack Dice', validators=[DataRequired(), NumberRange(min=1)])
    defend_dice = IntegerField('Defend Dice', validators=[DataRequired(), NumberRange(min=1)])
    starting_body_points = IntegerField('Starting Body Points', validators=[DataRequired(), NumberRange(min=1)])
    starting_mind_points = IntegerField('Starting Mind Points', validators=[DataRequired(), NumberRange(min=1)])
    weapons = StringField('Weapons', validators=[DataRequired()])
    armor = StringField('Armor', validators=[DataRequired()])
    body_points = IntegerField('Body Points', validators=[DataRequired(), NumberRange(min=1)])
    quests = IntegerField('Quests', validators=[DataRequired(), NumberRange(min=0)])
    gold_coins = IntegerField('Gold Coins', validators=[DataRequired(), NumberRange(min=0)])
    items = StringField('Items', validators=[DataRequired()])
    submit = SubmitField('Create Hero')
