from app import app
# from flask import Response, stream_with_context
# from flask import make_response
# from os.path import join
# import io
# from flask_restful import Resource


# purely to avoid pep8 errors
def initialize():
    pass


@app.route('/all')
def all_json():
    return 'hi'

"""    # def generate():
        # with io.open(join(app.static_folder, 'all.json'), 'rb') as fp:
            # yield fp.read(4096)

    # return Response(stream_with_context(generate()), mimetype='text/json')
"""
