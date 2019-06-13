#!/usr/bin/env python3

import os

from willamette_client.client import WillametteClient


def load_test_data():
    print("Loading test data")


def main():
    url = os.getenv('WILLAMETTE_API_URL', 'http://localhost:5000/api')
    client = WillametteClient(url)
    load_test_data()


if __name__ == 'main':
    main()
