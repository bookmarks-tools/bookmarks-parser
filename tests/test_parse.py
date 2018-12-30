import json
import os

import pytest
import bookmarks_parser

tests_data_path = (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tests_data'))


@pytest.fixture
def result_chrome():
    result_path = os.path.join(tests_data_path, 'chrome_bookmarks.json')
    with open(result_path, 'r') as f:
        return json.load(f)


def test_chrome(result_chrome):
    html_path = os.path.join(tests_data_path, 'chrome_bookmarks.html')
    assert bookmarks_parser.parse(html_path) == result_chrome
