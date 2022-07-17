
from flask import Flask, render_template

# template_folder defined for pythonanywhere vm
app = Flask(__name__, template_folder='/home/benaustin123/mysite/templates', static_url_path="/home/benaustin123/mysite/static", static_folder = 'static')

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


@app.route("/tierlist.html")
def display_tierlist():
    """
    Display tierlist maker

    Returns
    -------
    Flask render of html template
    """
    
    
    return render_template("tierlist.html")


@app.route("/ai_test.html")
def display_aitest():
    """
    Display ai test

    Returns
    -------
    Flask render of html template
    """
    
    
    return render_template("ai_test.html")

def test_func():
    return "testtestintesintesintesin"
