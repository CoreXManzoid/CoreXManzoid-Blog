from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email('Please enter a valid email.')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message='The password must be at least for 8 characters.')])
    name = StringField(label='Name', validators=[DataRequired()])
    submit = SubmitField('Sign Me Up!')
    
    
# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email('Please enter a valid email.')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message='The password must be at least for 8 characters.')])
    submit = SubmitField('Let Me In!')

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField('Leave a Comment', validators=[DataRequired()])
    submit = SubmitField('Submit Comment')