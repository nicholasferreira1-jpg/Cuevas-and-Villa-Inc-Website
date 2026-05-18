# Team of the Firm

from flask import Blueprint, render_template

# Create Blueprint

team_bp = Blueprint("team", __name__)

# Route

@team_bp.route("/team")
def team():
    return render_template("team.html")