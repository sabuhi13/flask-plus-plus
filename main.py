from flask import Flask
from app.services import user

app = Flask(__name__)

@app.route('/')
def index():
    return user.index()

if __name__ == '__main__':
    app.run(debug=True)