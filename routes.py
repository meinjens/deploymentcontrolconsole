from flask import Flask, url_for, request, render_template
from app import app


@app.route('/', methods=['GET'])
def hello():
    return 'Hello'


@app.route('/switch/list', methods=['GET'])
def get_switches():
    return '{}'


@app.route('/switch/<number>', methods=['GET'])
def get_switch(number):
    return '{}'


@app.route('/switch/<number>', methods=['PUT'])
def set_switch(number):
    return '{}'
