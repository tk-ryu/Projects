from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class ReviewForm(FlaskForm):
    subject = StringField('Rating', validators=[DataRequired("What's your rating?")])
    content = TextAreaField('Review', validators=[DataRequired('Please write reviews')])

class RecipeForm(FlaskForm):
    subject = TextAreaField('Subject', validators=[DataRequired('Enter subject')])
    time = TextAreaField('Time', validators=[DataRequired('Cooking time in minutes')])
    ingredients1 = TextAreaField('Ingredients', validators=[DataRequired('Ingredients')])
    ingredients2 = TextAreaField('Ingredients', validators=[DataRequired('Ingredients')])
    ingredients3 = TextAreaField('Ingredients', validators=[DataRequired('Ingredients')])
    ingredients4 = TextAreaField('Ingredients', validators=[DataRequired('Ingredients')])
    ingredients5 = TextAreaField('Ingredients', validators=[DataRequired('Ingredients')])
    tags = TextAreaField('Tags', validators=[DataRequired('Ingredients')])


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
    DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])

class OrderForm(FlaskForm):
    product_id = IntegerField('상품번호', validators=[DataRequired('상품번호는 필수입력 항목입니다.'), Length(min=6,max=6)])


class ChangePassword(FlaskForm):
    password1 = PasswordField('Password', validators=[DataRequired("New Password")])
    