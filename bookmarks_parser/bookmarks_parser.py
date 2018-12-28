import html5lib


def get_tag_name(tag):
    return tag[tag.rindex('}') + 1:]


def get_node_data(node):
    data = {}
    for child in node:
        tag_name = get_tag_name(child.tag)
        if tag_name == 'a':
            data['type'] = 'bookmark'
            data['url'] = child.get('href')
            data['title'] = child.text
            data['add_date'] = child.get('add_date')
            data['icon'] = child.get('icon')
        elif tag_name == 'h3':
            data['type'] = 'folder'
            data['title'] = child.text
            data['add_date'] = child.get("add_date")
            data['last_modified'] = child.get("last_modified")
        elif tag_name == "dl":
            data['__dir_dl'] = child
    return data


def process_dir(bookmark_dir):
    items = []
    for child in bookmark_dir:
        tag_name = get_tag_name(child.tag)
        if tag_name != "dt":
            continue
        item_data = get_node_data(child)
        if item_data.get('__dir_dl'):
            item_data['children'] = process_dir(item_data['__dir_dl'])
            del item_data['__dir_dl']
        items.append(item_data)
    return items


def parse(file_path):
    with open(file_path, "rb") as f:
        document = html5lib.parse(f)
    bookmarks = process_dir(document[1][1])
    return bookmarks
