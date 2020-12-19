from reader import read_books
from categorizer import categorize
from sort import sort_biblio
from writer import write_biblio

keynames = {'file':'file', 'directory':'directory'}

#分類済みのファイルはカテゴライズ
biblio_h = read_books('H:\\スキャン書籍', keynames)
categorize(biblio_h, 'H:\\スキャン書籍', 'directory', 'category')

#スキャン済みファイルは放置
biblio_f = read_books('F:\\ScanSnap', keynames)

biblio = biblio_h + biblio_f
sort_biblio(biblio, 'file')
write_biblio(biblio, {'file', 'category'}, 'out', 'ebooks.xlsx')
