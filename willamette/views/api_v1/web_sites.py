__all__ = ['WebSiteView']

import logging

from quaerere_base_flask.views.base import BaseView

from willamette.app_util import get_db
from willamette.models import WebSiteModel
from willamette_common.schemas import WebSiteSchema

LOGGER = logging.getLogger(__name__)


class WebSiteView(BaseView):
    def __init__(self):
        super().__init__(WebSiteModel, WebSiteSchema, get_db)
