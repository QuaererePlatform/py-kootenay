__all__ = ['arangodb', 'get_collections', 'get_db']

from flask_arango_orm import ArangoORM
from .models import WebSiteModel, WebPageModel

MODELS = [WebSiteModel, WebPageModel]

arangodb = ArangoORM()


def get_db():
    return arangodb.connection

def get_collections():
    for model in MODELS:
        yield model
