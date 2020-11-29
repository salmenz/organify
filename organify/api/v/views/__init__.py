#!/usr/bin/python3
""" Blueprint for app views with url prefix to /api/v1 """
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v')

from api.v.views.auth import *

