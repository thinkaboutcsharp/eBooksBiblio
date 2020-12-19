def categorize(biblio, root, directory_keyname, category_keyname):
    skip_len = len(root) + 1
    for book in biblio:
        directory = book[directory_keyname]
        structure = directory[skip_len:]
        category = structure.split('\\')
        book[category_keyname] = category
