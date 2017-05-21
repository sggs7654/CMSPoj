from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, TextAreaField
from wtforms.validators import Required, Length, Email, Regexp

class HomeTextForm(FlaskForm):
    caption_title = StringField('Caption title:', validators=[Required()])
    caption_text = TextAreaField('Caption text:', validators=[Required()])
    column1_title = StringField('Column1 title:', validators=[Required()])
    column1_text = TextAreaField('Column1 text:', validators=[Required()])
    column2_title = StringField('Column2 title:', validators=[Required()])
    column2_text = TextAreaField('Column2 text:', validators=[Required()])
    column3_title = StringField('Column3 title:', validators=[Required()])
    column3_text = TextAreaField('Column3 text:', validators=[Required()])
    submit = SubmitField('Comfirm')


class RecruitForm(FlaskForm):
    recruit_title = StringField('Caption title:', validators=[Required()])
    recruit_text = TextAreaField('Caption text:', validators=[Required()])
    submit = SubmitField('Comfirm')


