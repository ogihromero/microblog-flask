from flask import Flask

app = Flask(__name__)

# Import realizado no final para evitar import circular
from app import routes
