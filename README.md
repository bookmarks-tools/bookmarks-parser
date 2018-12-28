# bookmarks-parser

Parsing Netscape bookmark export files.

## Installation
```
$ pip install git+https://github.com/andriyor/bookmarks-parser.git#egg=bookmarks-parser
```

### Installation from source
```
$ git clone https://github.com/andriyor/bookmarks-parser.git
$ cd bookmarks-parser
$ python setup.py install
```

## Usage

```
import pprint
import bookmarks_parser

bookmarks = bookmarks_parser.parse("bookmarks.html")
pprint.pprint(bookmarks)
```

## Development
Install [Pipenv](https://docs.pipenv.org/)
```
$ pipenv install --dev -e .
```