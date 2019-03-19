__all__ = ['register_views']

import sys, inspect

from flask_classful import FlaskView

from .web_pages import *
from .web_sites import *


def _view_classes():
    for cls in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        if issubclass(cls[1], FlaskView) and cls[0] != 'FlaskView':
            yield cls[1]


def register_views(app):
    for view in _view_classes():
        view.register(app, route_prefix='api/v1')
