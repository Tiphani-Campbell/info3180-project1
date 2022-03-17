from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    num_rooms = StringField('No. of Rooms', validators=[DataRequired()])
    num_bath = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    prop_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Image files only'])])
