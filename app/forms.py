from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class ProxyForm(FlaskForm):
    link = StringField('Link', [InputRequired('A URL is required.')],  render_kw={"placeholder": "http://"})
