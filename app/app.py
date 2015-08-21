#!/usr/bin/env python
"""
docstring app/app.py

"""
from flask import Flask
from .. import config


app = Flask(__name__)
app.config.from_object(config['development'])


def main():
    pass

if __name__ == "__main__":
    main()
    pass
