__all__ = ['WebPageView']

import logging

from quaerere_base_flask.views.base import BaseView

from willamette.app_util import get_db
from willamette.models import WebPageModel
from willamette_common.schemas import WebPageSchema

LOGGER = logging.getLogger(__name__)


class WebPageView(BaseView):
    def __init__(self):
        super().__init__(WebPageModel, WebPageSchema, get_db)
