def bmp2text():
    _path = input('输入bmp图片路径：').replace("'","")
    if _path[-1:] == ' ':
        _path = _path[:-1]
    with open(_path, 'rb') as _f:
        _everything = _f.read()

    _text = _everything[54:].replace(b'\x00', b'').decode('utf-8')
    print(_text)


if __name__ == '__main__':
    bmp2text()
