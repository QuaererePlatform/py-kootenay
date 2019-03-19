__all__ = ['WebSiteView']

import logging

from arango.exceptions import DocumentInsertError
from flask import jsonify, request
from flask_classful import FlaskView

from willamette.db import get_db
from willamette.db.models.web_sites import WebSiteModel
from willamette.schemas import db_metadata_schema
from willamette.schemas.web_sites import WebSiteSchema

LOGGER = logging.getLogger(__name__)


class WebSiteView(FlaskView):
    _schema = WebSiteSchema()
    _schema_many = WebSiteSchema(many=True)

    def index(self):
        db = get_db()
        web_sites = db.query(WebSiteModel).all()
        return jsonify(self._schema_many.dump(web_sites).data)

    def get(self, key):
        db = get_db()
        web_site = db.query(WebSiteModel).by_key(key)
        return jsonify(self._schema.dump(web_site).data)

    def post(self):
        if request.data:
            LOGGER.debug(f'Received POST data', extra={'data': request.data})
        unmarshal = self._schema.load(request.get_json())
        if len(unmarshal.errors) == 0:
            db = get_db()
            try:
                result = db.add(unmarshal.data)
                return jsonify(db_metadata_schema.dump(result).data), 201
            except DocumentInsertError as e:
                return jsonify({'errors': e.error_message}), e.http_code
        else:
            return jsonify({'errors': unmarshal.errors}), 400

    def is_downloaded(self, key, cc_index_id):
        pass
