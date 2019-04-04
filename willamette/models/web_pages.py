__all__ = ['WebPageModel']
import logging

from arango_orm import Collection
from arango_orm.fields import String, Url
from arango_orm.references import relationship

from .web_sites import WebSiteModel

LOGGER = logging.getLogger(__name__)


class WebPageModel(Collection):
    __collection__ = 'WebPages'
    _index = [{'type': 'hash', 'fields': ['url'], 'unique': True}]

    url = Url(required=True)
    web_site_key = String()
    web_site = relationship(WebSiteModel, 'web_site_key')
    text = String()
