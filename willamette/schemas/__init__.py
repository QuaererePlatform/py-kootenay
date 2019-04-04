__all__ = ['db_metadata_schema', 'WebPageSchema', 'WebSiteSchema']

from marshmallow import fields

from willamette.app_util import marshmallow
from .web_pages import WebPageSchema
from .web_sites import WebSiteSchema


class DBMetadata(marshmallow.Schema):
    _id = fields.String()
    _key = fields.String()
    _rev = fields.String()


db_metadata_schema = DBMetadata()
