"""

"""
__all__ = ['create_app']

from flask import Flask

from .db import arangodb
from .db.cli import db_cli
from .schemas import marshmallow
from .views.api_v1 import register_views


def create_app():
    app = Flask(__name__)
    app.config.from_object('willamette.config.flask_config')
    marshmallow.init_app(app)
    arangodb.init_app(app)

    register_views(app)

    app.cli.add_command(db_cli)

    return app
