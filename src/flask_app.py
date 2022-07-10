
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='/home/benaustin123/mysite/templates')

# GLOBAL VARS
TEMPLATE_PATHS = r"./templates"

@app.route('/')
def display_home():
    """
    Display home when routed to homepage

    Returns
    -------
    Flask render of html template
    """
    
    print(os.path.abspath(TEMPLATE_PATHS))
    return render_template("home.html")


def test_func():
    return "testtestintesintesintesin"
