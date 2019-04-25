from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, url


class ProxyForm(FlaskForm):
    link = URLField('Link', [InputRequired(), url()],  render_kw={"placeholder": "http://"})

