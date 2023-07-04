def bw2text():
    _path = input('输入BMP/WAV路径：')
    with open(_path, 'rb') as _f:
        _everything = _f.read()
        if _path.split('.')[-1] == 'bmp':
            _text = _everything[54:].replace(b'\x00', b'').decode('utf-8')
        elif _path.split('.')[-1] == 'wav':
            _text = _everything[44:].decode('utf-8')
    print(_text)

if __name__ == '__main__':
    bw2text()
