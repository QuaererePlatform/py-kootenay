"""Create and setup the Flask app
"""
__all__ = ['create_app']

from flask import Flask

from .app_util import arangodb, marshmallow
from .cli.db import db_cli
from .views.api_v1 import register_views


def create_app():
    """Flask app factory

    :return: Flask app instance
    :rtype: Flask
    """
    app = Flask(__name__)
    app.config.from_object('willamette.config.flask_config')
    marshmallow.init_app(app)
    arangodb.init_app(app)

    register_views(app)

    app.cli.add_command(db_cli)

    return app
