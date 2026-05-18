# Reviews page

from flask import Blueprint, render_template

# Create Blueprint

reviews_bp = Blueprint("reviews", __name__)

# Route

@reviews_bp.route("/reviews")
def reviews():
    return render_template("reviews.html")