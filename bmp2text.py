def bmp2text():
    _path = input('输入bmp图片绝对路径：')
    with open(_path, 'rb') as _f:
        _everything = _f.read()

    _text = _everything[54:].replace(b'\x00', b'').decode('utf-8')
    print(_text)


if __name__ == '__main__':
    bmp2text()
