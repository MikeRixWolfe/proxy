from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ProxyForm(FlaskForm):
    link = StringField('Link', validators=[DataRequired()])
