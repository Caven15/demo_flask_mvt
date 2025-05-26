from flask import Flask

# Initialisation de l'application flask
app = Flask(__name__)

from app.routes import other, task