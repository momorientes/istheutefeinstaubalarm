#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify 
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    alarm = parse_widget(get_widget())
    return render_template('index.html', alarm=alarm)

@app.route('/api/alarm')
def api_alarm():
    alarm = parse_widget(get_widget())
    return jsonify({'feinstaubalarm': alarm})

def parse_widget(data):
    soup = BeautifulSoup(data, 'html.parser')
    if soup.find('div', {'class': 'alarm-on'}):
        return True
    else:
        return False

def get_widget():
    text = requests.get('http://www.stuttgart.de/feinstaubalarm/widget/xtrasmall').text
    return text 

if __name__ == '__main__':
    app.run()

