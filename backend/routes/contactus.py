# Contact us Page

from flask import Blueprint, render_template

# Create Blueprint

contactus_bp = Blueprint("contactus", __name__)

# Route

@contactus_bp.route("/contactus")
def contactus():
    return render_template("contactus.html")