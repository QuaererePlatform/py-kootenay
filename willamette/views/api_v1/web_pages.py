__all__ = ['WebPageView']

import logging

from arango.exceptions import DocumentInsertError
from flask import jsonify, request
from flask_classful import FlaskView

from willamette.db import get_db
from willamette.db.models.web_sites import WebPageModel
from willamette.schemas import db_metadata_schema
from willamette.schemas.web_sites import WebPageSchema

LOGGER = logging.getLogger(__name__)


class WebPageView(FlaskView):
    _schema = WebPageSchema()
    _schema_many = WebPageSchema(many=True)

    def index(self):
        db = get_db()
        web_pages = db.query(WebPageModel).all()
        return jsonify(self._schema_many.dump(web_pages).data)

    def get(self, key):
        db = get_db()
        web_page = db.query(WebPageModel).by_key(key)
        return jsonify(self._schema.dump(web_page).data)

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
