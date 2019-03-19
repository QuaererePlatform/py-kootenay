__all__ = ['WebSiteModel']

import logging

from arango_orm import Collection
from arango_orm.fields import String, Url

LOGGER = logging.getLogger(__name__)


class WebSiteModel(Collection):
    __collection__ = 'WebSites'
    _index = [{'type': 'hash',
               'fields': ['url', 'inLanguage'],
               'unique': True}]

    url = Url(required=True)
    inLanguage = String()
