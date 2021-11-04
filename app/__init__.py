from flask import Flask
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.run(debug=True)
from app import routes
