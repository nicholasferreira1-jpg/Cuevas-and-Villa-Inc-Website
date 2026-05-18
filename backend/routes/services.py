# Services page

from flask import Blueprint, render_template

# Create Blueprint

services_bp = Blueprint("services", __name__)

# Route

@services_bp.route("/services")
def services():
    return render_template("services.html")