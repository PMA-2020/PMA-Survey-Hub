"""App"""
from flask import Flask

from .routes import routes


def create_app():
    """Create configured Flask application.

    Returns:
        Flask: Configured Flask application.
    """
    app = Flask(__name__)
    app.register_blueprint(routes)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
