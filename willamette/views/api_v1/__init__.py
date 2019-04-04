"""Module for version 1 of the API
"""
__all__ = ['register_views']

import sys, inspect

from flask_classful import FlaskView

from .web_pages import *
from .web_sites import *


def _view_classes():
    """Generator for accessing imported FlaskView classes

    :return: Yields FlaskView classes
    :rtype: [FlaskView]
    """
    for cls in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        if issubclass(cls[1], FlaskView) and cls[0] != 'FlaskView':
            yield cls[1]


def register_views(app):
    """Registers FlaskView classes to the Flask app passed as argument

    :param app: Flask app instance
    :type app: flask.Flask
    :return:
    """
    for view in _view_classes():
        view.register(app, route_prefix='api/v1')
