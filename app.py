from flask import Flask, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from helpers import *
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GREAT_PASSWORD'
debug = DebugToolbarExtension(app)

valid_codes = []

def get_codes():
    response = requests.get('https://api.exchangerate.host/symbols')
    data = response.json()
    valid_codes.extend(list(data['symbols'].keys()))
    
@app.route('/')
def home():
    return render_template('app.html')

@app.route('/convert')
def convert():   
    get_codes()
    # print(valid_codes)

    currency_from = request.args['from'].upper()
    currency_to = request.args['to'].upper()
    currency_amount = request.args['amount']
    # print(currency_from)
    # print(currency_to)
    # print(currency_amount)

    if currency_from in valid_codes and currency_to in valid_codes:
        if is_float(currency_amount):
            url = f'https://api.exchangerate.host/convert?from={currency_from}&to={currency_to}&amount={currency_amount}'
            response = requests.get(url)
            data = response.json()
            try:
                currency_converted = round((data['result']), 2)
            except TypeError:
                flash('Please enter a valid amount', 'invalid')
                return render_template('failed.html')
            # return data
            return render_template('success.html', amount = data['query']['amount'], currency_from = currency_from, currency_converted = currency_converted, currency_to = currency_to)
        if not is_float(currency_amount):
            flash('Please enter a valid amount', 'invalid')
    if currency_from not in valid_codes:
        flash('Please enter a valid currency code to convert from', 'invalid')
    if currency_to not in valid_codes:
        flash('Please enter a valid currency code to convert to', 'invalid')
    return render_template('failed.html')
