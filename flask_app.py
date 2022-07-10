
# A very simple Flask Hello World app for you to get started with...
# control-shift-g to open source control
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello austy'

