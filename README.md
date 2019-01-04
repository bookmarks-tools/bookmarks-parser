# bookmarks-parser
[![Build Status](https://travis-ci.org/andriyor/bookmarks-parser.svg?branch=master)](https://travis-ci.org/andriyor/bookmarks-parser)
[![codecov](https://codecov.io/gh/andriyor/bookmarks-parser/branch/master/graph/badge.svg)](https://codecov.io/gh/andriyor/bookmarks-parser)
[![image](https://img.shields.io/pypi/v/bookmarks-parser.svg)](https://pypi.org/project/bookmarks-parser/)
[![image](https://img.shields.io/pypi/l/bookmarks-parser.svg)](https://pypi.org/project/bookmarks-parser/)
[![image](https://img.shields.io/pypi/pyversions/bookmarks-parser.svg)](https://pypi.org/project/bookmarks-parser/)

Parsing Netscape bookmark (Google Chrome, Firefox, ... export files) .

## Installation
```
$ pip install bookmarks-parser
```

## Usage
```python
import pprint
import bookmarks_parser

bookmarks = bookmarks_parser.parse("bookmarks.html")
pprint.pprint(bookmarks)
```
[output example](https://github.com/andriyor/bookmarks-parser/tree/master/tests/tests_data)

## Development
Install [Poetry](https://poetry.eustace.io/docs/)   
```
$ poetry install
```
run tests
```
$ poetry run pytest --cov=bookmarks_parser
```

## License
[MIT](https://choosealicense.com/licenses/mit/)