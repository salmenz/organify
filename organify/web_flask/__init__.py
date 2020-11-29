#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')
