from datetime import date
from flask import render_template, flash, redirect
from app import app
from .forms import ProxyForm
from .util import getData


@app.route('/proxy', strict_slashes=False, methods=['GET','POST'])
def index():
    form = ProxyForm()

    if form.validate_on_submit():
        return redirect('/proxy/{}'.format(form.link.data.strip()))

    if form.errors:
        if isinstance(form.errors, dict):
            flash(form.errors.values()[0][0], 'danger')

    return render_template('index.html',
                           year=date.today().year,
                           form=form)


@app.route('/proxy/<path:source_url>', methods=['GET'])
def proxy(source_url):
    title, header, body = getData(source_url)
    page = { 'header': header, 'body': body }

    return render_template('proxy.html',
                           title=title,
                           page=page)

