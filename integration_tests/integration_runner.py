#!/usr/bin/env python3


import logging
import os
import pathlib
import yaml

import arango
from willamette_client.client import WillametteClient

LOGGER = logging.getLogger()
WILLAMETTE_API_URL = 'http://web_app:5000/api'
WEB_SITE_DB_COLLECTION = 'WebSites'
DATA_FILE = pathlib.Path('test_data.yaml')
ARANGODB_ROOT_PASSWORD = os.getenv('ARANGODB_ROOT_PASSWORD')
ARANGODB_USER = os.getenv('ARANGODB_USER')
ARANGODB_PASSWORD = os.getenv('ARANGODB_PASSWORD')
DB_NAME = 'quaerere'


def load_test_data():
    with open(DATA_FILE) as yaml_file:
        return yaml.safe_load(yaml_file)


def get_willamette_client():
    url = os.getenv('WILLAMETTE_API_URL', WILLAMETTE_API_URL)
    client = WillametteClient(url)
    return client


def get_arango_conn():
    a_client = arango.ArangoClient(protocol='http', host='test_db', port=8529)
    db_conn = a_client.db(DB_NAME,
                          ARANGODB_USER,
                          ARANGODB_PASSWORD)
    if db_conn.ping() != 200:
        raise Exception(f'Unable to connect to {DB_NAME}')
    return db_conn


def get_arango_root_conn():
    a_client = arango.ArangoClient(protocol='http', host='test_db', port=8529)
    db_conn = a_client.db('_system',
                          'root',
                          ARANGODB_ROOT_PASSWORD)
    if db_conn.ping() != 200:
        raise Exception(f'Unable to connect to _system')
    return db_conn


def setup_db(test_data):
    root_conn = get_arango_root_conn()
    root_conn.create_user(ARANGODB_USER, ARANGODB_PASSWORD)
    root_conn.create_database(DB_NAME)
    q_db = get_arango_conn()
    q_db.create_collection(WEB_SITE_DB_COLLECTION)

    web_sites = q_db.collection(WEB_SITE_DB_COLLECTION)
    for web_site in test_data['web_sites']:
        web_sites.insert(web_site)


def main():
    test_data = load_test_data()
    setup_db(test_data)


if __name__ == '__main__':
    main()
