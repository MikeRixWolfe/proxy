import requests
from bs4 import BeautifulSoup
from breadability.readable import Article
from datetime import date
from flask import render_template, flash, redirect
from app import app
from .forms import ProxyForm


@app.route('/proxy', strict_slashes=False, methods=['GET','POST'])
def index():
    form = ProxyForm()
    if form.validate_on_submit():
        flash('Proxying {}'.format(form.link.data))
        return redirect('/proxy/{}'.format(form.link.data))

    return render_template('index.html',
                           year=date.today().year,
                           form=form)


@app.route('/proxy/<path:source_url>', methods=['GET'])
def proxy(source_url):
    flash('Proxying {}'.format(source_url))

    title, header, body = getData(source_url)
    page = { 'header': header, 'body': body }

    return render_template('proxy.html',
                           title=title,
                           page=page)


def getData(source_url):
    if not source_url.startswith('//') and '://' not in source_url:
        source_url = 'http://' + source_url

    try:
        html = requests.get(source_url, headers={'User-Agent': 'Computer Club Plaintext Reading Plugin'}).text
    except:
        return None, None, None

    soup = BeautifulSoup(html, 'lxml')

    try:
        header = soup.find('h1').text.strip()
    except:
        header = None

    try:
        title = soup.find('title').text.strip()
    except:
        title = None

    readable = Article(html, url=source_url).readable
    soup = BeautifulSoup(readable, 'lxml')

    if not soup.find('div', {'id': 'readabilityBody'}).text.strip():
        readable = None

    return title, header, readable

