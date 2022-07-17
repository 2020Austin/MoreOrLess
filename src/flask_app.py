
from flask import Flask, render_template

# template_folder defined for pythonanywhere vm
app = Flask(__name__, template_folder='/home/benaustin123/mysite/templates')

# GLOBAL VARS


@app.route("/")
def display_home():
    """
    Display home when routed to homepage

    Returns
    -------
    Flask render of html template
    """
    
    return render_template("home.html")


@app.route("/tierlist")
def display_tierlist():
    return render_template("tierlist.html")

def test_func():
    return "testtestintesintesintesin"
