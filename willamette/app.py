"""Create and setup the Flask app
"""
__all__ = ['create_app']

import logging

from flask import Flask

from .app_util import arangodb, marshmallow
from .cli.db import db_cli
from .views.api_v1 import register_views


LOGGER = logging.getLogger(__name__)


def create_app(*args, **kwargs):
    """Flask app factory

    :return: Flask app instance
    :rtype: Flask
    """
    LOGGER.debug(f'Flask startup; args: {args}, kwargs: {kwargs}')
    app = Flask(__name__)
    app.config.from_object('willamette.config.flask_config')
    marshmallow.init_app(app)
    arangodb.init_app(app)

    register_views(app)

    app.cli.add_command(db_cli)

    return app
