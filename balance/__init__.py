from flask import Flask

app = Flask(__name__)
app.secret_key = b'supersegura'


from balance.routes import *




