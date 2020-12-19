def read_books(parent, keynames):
    import os
    import os.path
    from toutf8 import toutf8

    parent = toutf8(parent)

    if not os.path.exists(parent):
        print('parent no exists!')
        return []

    biblio = []

    for child in os.listdir(parent):
        child = toutf8(child)
        full_child = os.path.join(parent, child)
        
        if os.path.isdir(full_child):
            if child == '.organizer' or child.startswith('!'):
                continue
            
            biblio.extend(read_books(full_child, keynames))
        
        elif os.path.isfile(full_child):
            if not child.endswith('.pdf') or child.startswith('._'):
                continue
            if child == 'old.pdf':
                continue
            
            child = child.replace('%20', ' ')
            biblio.append({ keynames['file']: child, keynames['directory']: parent })
    
    return biblio


if __name__ == '__main__':
    biblio = read_books('F:\\ScanSnap', {'file': 'file', 'directory': 'directory'})
    for book in biblio:
        print(book)
    print(len(biblio))