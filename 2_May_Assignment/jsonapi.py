# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:14:02 2022

@author: suman
"""
import flask
from flask import request, jsonify, Flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

books = [
    {'id': 0, 
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first sentence': "The coldsleep itself was dreamless.",
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, brigh',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
    ]

@app.route('/', methods=['GET'])

def home():
    return 'hello to my api' 

@app.route('/books/all', methods=['GET'])

def api_all():
    return jsonify (books)

app.run()