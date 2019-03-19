__all__ = ['marshmallow', 'db_metadata_schema']

from flask_marshmallow import Marshmallow
from marshmallow import fields

marshmallow = Marshmallow()


class DBMetadata(marshmallow.Schema):
    _id = fields.String()
    _key = fields.String()
    _rev = fields.String()

db_metadata_schema = DBMetadata()
