import json
import pathlib

import pytest
import bookmarks_parser

tests_data_path = pathlib.Path(__file__).parent.resolve() / 'tests_data'


@pytest.fixture
def result_chrome():
    with open(tests_data_path / 'chrome_bookmarks.json', 'r') as f:
        return json.load(f)


def test_chrome(result_chrome):
    assert bookmarks_parser.parse(tests_data_path / 'chrome_bookmarks.html') == result_chrome
