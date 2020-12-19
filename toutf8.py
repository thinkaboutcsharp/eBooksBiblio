def toutf8(str):
    import chardet
    str_bytes = str.encode()
    encoding = chardet.detect(str_bytes)
    if encoding['encoding'] != 'utf-8' and encoding['encoding'] != 'ascii' and encoding['encoding'] != 'Windows-1252' and encoding['encoding'] != 'IBM866':
        bytes = str.encode(encoding['encoding'])
        result = bytes.decode('utf-8')
    else:
        result = str
    
    return result
