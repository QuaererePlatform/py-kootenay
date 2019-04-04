__all__ = ['WebPageSchema']

from marshmallow import fields, post_load

from willamette.app_util import marshmallow
from willamette.models import WebPageModel


class WebPageSchema(marshmallow.Schema):

    text = fields.String()
    url = fields.Url(required=True)
    web_site_key = fields.String()
    _key = fields.String()

    @post_load
    def make_web_page(self, data):
        return WebPageModel(**data)
