from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GREAT_PASSWORD'
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/convert')
def convert():
    key = request.args
    print(key)
    return render_template('app.html')
