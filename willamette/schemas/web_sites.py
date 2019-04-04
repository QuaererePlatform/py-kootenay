__all__ = ['WebSiteSchema']

from marshmallow import fields, post_load

from willamette.app_util import marshmallow
from willamette.models import WebSiteModel


class WebSiteSchema(marshmallow.Schema):

    url = fields.Url(required=True)
    inLanguage = fields.String()
    _key = fields.String()

    @post_load
    def make_web_site(self, data):
        return WebSiteModel(**data)
