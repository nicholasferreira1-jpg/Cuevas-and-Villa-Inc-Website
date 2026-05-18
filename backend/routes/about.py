# About us page

from flask import Blueprint, render_template

# Create Blueprint

about_bp = Blueprint("aboutus", __name__)

# Route

@about_bp.route("/aboutus")
def about():
    return render_template("about.html")