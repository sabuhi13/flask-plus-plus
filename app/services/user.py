from flask import render_template
from app.models import user

def index():
    return render_template('index.html')