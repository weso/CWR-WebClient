from flask import Flask

__author__ = 'Bernardo'

app = Flask(__name__)

from webapp.view import views
