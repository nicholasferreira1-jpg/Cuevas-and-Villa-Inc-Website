# Database structure

from app import db

# Table that stores everyone that adds their informations to contact the firm. 
""" Contains: 
id for every client,
full name, 
email, 
phone number, 
service, 
description, 
meeting type.
"""
# db Model used to tell SQLAlchemy this is a table
class Client(db.Model):
    # Table Name in PostgreSQL
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(100), nullable = True)
    service = db.Column(db.String(100), nullable = False)
    date_signed_up = db.Column(db.DateTime, default=db.func.current_timestamp())
    meeting_type = db.Column(db.String(50), nullable = False, default = "In Person")

    def __repr__(self):
        return f"Client: {self.name} - {self.service}"
