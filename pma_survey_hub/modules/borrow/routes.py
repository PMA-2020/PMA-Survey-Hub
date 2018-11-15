"""Web application for XFormTest

http://xform-test.pma2020.org
"""
import platform
import os
import flask
from flask import render_template, request, send_file, Blueprint

# noinspection PyProtectedMember
from .static_methods import _run_background_process, upload_file
from .config import template, PKG_NAME, settings

routes = Blueprint(PKG_NAME, __name__)
basedir = os.path.abspath(os.path.dirname(__file__))
path_char = '\\' if platform.system() == 'Windows' else '/'


@routes.route('/', methods=['GET', 'POST'])
def index():
    """Index"""
    if flask.request.method == 'GET':
        return render_template(template, **settings)
    else:
        try:
            base_files = flask.request.files.getlist("sources[]")
            base_file_names = ''
            for base_file in base_files:
                base_file_name = upload_file(base_file)
                base_file_names += ' '+base_file_name
            target_origin = request.files['target']
            target_file = upload_file(target_origin)
            '''options_list = request.form.getlist('options[]')
            options = " ".join(options_list)'''

            command = "python -m pmix.borrow -m " + target_file + " " +\
                      base_file_names
            stdout, stderr = _run_background_process(command)
            return render_template(template, stderr=stderr, stdout=stdout,
                                   target_file_path=target_file,
                                   target_file_name=target_origin.filename,
                                   **settings)

        except Exception as err:
            msg = 'An unexpected error occurred:\n\n' + str(err)
            return render_template(template, stderr=msg, **settings)


@routes.route('/export', methods=['POST'])
def export():
    """Export"""
    target_file_path = request.form['target_file_path']
    target_file_name = request.form['target_file_name']
    return send_file(target_file_path, None, True, target_file_name)
