def sort_biblio(biblio, sort_key):
    import operator

    biblio.sort(key=operator.itemgetter(sort_key))


if __name__ == '__main__':
    from reader import read_books
    from writer import write_biblio
    biblio = read_books('F:\\ScanSnap')
    sort_biblio(biblio, 'file')
    keys = ['file', 'directory']
    write_biblio(biblio, keys, 'out', 'scan.xlsx')