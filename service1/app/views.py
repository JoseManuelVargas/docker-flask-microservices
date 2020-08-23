import requests
from flask import render_template

from app import app

@app.route('/')
def home():
    response = requests.get('http://service2/api1')
    return render_template('index.html', result=response.json())

