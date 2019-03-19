__all__ = ['db_cli']

import logging

from flask.cli import AppGroup

from willamette.db import arangodb, get_collections

LOGGER = logging.getLogger(__name__)

db_cli = AppGroup('db')


@db_cli.command('init')
def init_db():
    db = arangodb.connection
    LOGGER.info('Initializing database')
    for collection in get_collections():
        if not db.has_collection(collection):
            LOGGER.info(f'Creating collection: {collection}')
            db.create_collection(collection)
