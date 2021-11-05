from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, IntegerField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine','porcupine')])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(0,30,'age must be between 0 and 30'), Optional()])
    notes = TextAreaField("Notes")
    
class EditPetForm(FlaskForm):
    """ Form for editing pet data """

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available", default='checked')
    