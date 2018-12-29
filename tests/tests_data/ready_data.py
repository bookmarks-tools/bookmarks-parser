import json
import pathlib
import bookmarks_parser

tests_data_path = pathlib.Path(__file__).parent.resolve()
bookmarks = bookmarks_parser.parse(tests_data_path / 'chrome_bookmarks.html')
with open(tests_data_path / 'chrome_bookmarks.json', 'w') as fp:
    json.dump(bookmarks, fp, indent=2)
