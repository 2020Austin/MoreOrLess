
from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template("home.html", template_folder=TEMPLATE_PATHS)


def test_func():
    return "testtestintesintesintesin"
