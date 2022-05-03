# -*- coding: utf-8 -*-
"""
Created on Mon May  2 12:45:05 2022

@author: suman
"""

from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] == True

@app.route("/", methods = ['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

app.run()


