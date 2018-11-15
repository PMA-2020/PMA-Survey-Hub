"""xlsdiff"""
import flask
from flask import render_template, request, Blueprint

# noinspection PyProtectedMember
from .static_methods import _run_background_process, upload_file
from .config import template, PKG_NAME, settings

routes = Blueprint(PKG_NAME, __name__)


@routes.route('/', methods=['GET', 'POST'])
def index():
    """Index"""
    if flask.request.method == 'GET':
        return render_template(template, **settings)
    else:
        try:
            base_file = upload_file(request.files['base-file'])
            new_file = upload_file(request.files['new-file'])
            options_list = request.form.getlist('options[]')
            options = " ".join(options_list)

            command = "python -m pmix.xlsdiff " + base_file + " " + \
                      new_file + " " + options
            stdout, stderr = _run_background_process(command)
            return render_template(template, stderr=stderr, stdout=stdout,
                                   **settings)

        except Exception as err:
            msg = 'An unexpected error occurred:\n\n' + str(err)
            return render_template(template, stderr=msg, **settings)
