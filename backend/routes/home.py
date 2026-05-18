# Home page

from flask import Blueprint, render_template

# Create Blueprint

home_bp = Blueprint("home", __name__)

# Route

@home_bp.route("/")
def home():
    return render_template("index.html")