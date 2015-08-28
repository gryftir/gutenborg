from app import app
# from flask_restful import reqparse, abort, Api, Resource


# purely to avoid pep8 errors
def initialize():
    pass


@app.route('/all')
def all_json():
    return app.send_static_file('all.json')
