from reader import read_books
from categorizer import categorize
from sort import sort_biblio
from writer import write_biblio

keynames = {'file':'file', 'directory':'directory'}

#分類済みのファイルはカテゴライズ
biblio_h = read_books('H:\\スキャン書籍', keynames)
categorize(biblio_h, 'H:\\スキャン書籍', 'directory', 'category')

biblio_g = read_books('G:\\洋書ダウンロード', keynames)
categorize(biblio_g, 'G:\\洋書ダウンロード', 'directory', 'category')

#スキャン済みファイルは放置
biblio_f = read_books('F:\\ScanSnap', keynames)

#ダウンロード系は放置
biblio_d = read_books('H:\\eBooks', keynames)

biblio = biblio_h + biblio_f + biblio_g + biblio_d
sort_biblio(biblio, 'file')
write_biblio(biblio, ['file', 'category'], 'out', 'ebooks.xlsx')
