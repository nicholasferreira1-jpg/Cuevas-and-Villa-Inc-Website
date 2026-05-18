# Flask application, database, routes, start server 

from flask import Flask, render_template, request
from flask_sqlachemy import SQLAlchemy
import config

# Flask application

app = Flask(
    __name__, 
    template_folder = "../frontend/templates",
    static_folder = "../frontend/static"
)

app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize database

db = SQLAlchemy(app)

# Register Routes

from routes.home import home_bp
from routes.about import about_bp
from routes.services import services_bp
from routes.team import team_bp
from routes.reviews import reviews_bp
from routes.contactus import contactus_bp

app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(services_bp)
app.register_blueprint(team_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(contactus_bp)

# Created the table structured in models.py
with app.app_context():
    db.create_all()

# Start server
if __name__ == "__main__":
    app.run(debug = True)
