#!/usr/bin/env python
"""
docstring app/models.py

"""
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    pubyear = db.Column(db.Date())
    fields = db.Column(JSON)


def initialize():
    pass
