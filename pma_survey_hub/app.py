"""Definition of application object."""
import os

from flask import Blueprint, Flask, render_template
from flask_cors import CORS

from flask_adminlte import AdminLTE
from .config import config, get_settings

root = Blueprint('root', __name__)


@root.route('/')
def index():
    """Root route.

    .. :quickref: Root; Redirects to resources list or documentation depending
     on MIME type

    Args:
        n/a
    """
    return render_template(
        'core_modules/welcome/index.html',
        module_name=get_settings('App Short-Title'),
        page_name="Welcome",
        # icon="fa fa-star-o",
        module_abbreviation="Home",
        app_config_settings=get_settings(),
        messages=[],
        notifications=[],
        current_user='',
        logged_in=True)


def create_app(config_name=os.getenv('FLASK_CONFIG', 'default')):
    """Create configured Flask application.

    Args:
        config_name (str): Name of the configuration to be used.

    Returns:
        Flask: Configured Flask application.
    """
    # noinspection PyShadowingNames
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    AdminLTE(app)
    app.register_blueprint(root)

    from .modules.xform_test.routes import routes as xform_test
    app.register_blueprint(xform_test, url_prefix='/xform-test')
    from .modules.xlsdiff.routes import routes as xlsdiff
    app.register_blueprint(xlsdiff, url_prefix='/xlsdiff')
    from .modules.borrow.routes import routes as borrow
    app.register_blueprint(borrow, url_prefix='/borrow')

    from .modules.ppp.routes import routes as ppp
    app.register_blueprint(ppp, url_prefix='/ppp')
    # from .modules.ppp.app import add_views
    # add_views(app, '/ppp')

    return app
