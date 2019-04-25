from datetime import date
from flask import render_template, flash, redirect
from requests import get

from app import app
from .forms import ProxyForm


UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

@app.route('/proxy', strict_slashes=False, methods=['GET','POST'])
def index():
    form = ProxyForm()

    if form.validate_on_submit():
        return redirect('/proxy/{}'.format(form.link.data.strip()))

    if form.errors:
        if isinstance(form.errors, dict):
            flash(form.errors.values()[0][0], 'danger')

    return render_template('index.html',
                           form=form)


@app.route('/proxy/<path:source_url>', methods=['GET'])
def proxy(source_url):
    return get(source_url, headers={'User-Agent': UA}).content

