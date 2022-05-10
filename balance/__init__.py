from flask import Flask

app = Flask(__name__)
app.secret_key = b'supersegura'
app.config.from_object("config")

from balance.routes import *




