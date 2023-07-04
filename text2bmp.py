import re
import math


def small_hex(_n):
    _n = hex(_n)
    if len(_n) % 2 != 0:
        _n = '0' + _n
    _n = re.findall(r'.{2}', _n.replace('0x', ''))[::-1]
    if len(_n) < 4:
        _n = _n + ['00'] * (4 - len(_n))
    _n = ''.join(_n)
    return _n


# 计算长宽
def w_h_calc(_data_encoded):
    _data_origin_len = math.ceil(len(_data_encoded) / 3)
    _w = _h = round(_data_origin_len ** 0.5)
    if _w * _h < _data_origin_len:
        if _w * (_h + 1) >= _data_origin_len:
            _w = _w
            _h = _h + 1
        else:
            _w = _w + 1
            _h = _h + 1
    else:
        _w = _w
        _h = _h
    return _w, _h


def ins_0(_w, _h, _data_encoded):
    _i = _j = 0
    _new_data = b''
    _pic_area = _w * _h * 3
    while _i + _w * 3 <= _pic_area:
        # 每行有w * 3个byte
        _i += _w * 3
        # 对每行进行补0，使其长度可以被4整除
        _row_len_tar = math.ceil(_w * 3 / 4) * 4
        _new = _data_encoded[_j:_i] + (_row_len_tar - len(_data_encoded[_j:_i])) * int('00', 16).to_bytes(1, 'big')
        _new_data += _new
        _j = _i
    return _new_data


def gen_head(_size, _w, _h):
    # 生成16进制
    _size = small_hex(_size)
    _w = small_hex(_w)
    _h = small_hex(_h)
    _head = f'424D,{_size[:4]},{_size[4:]},0000,0000,3600,0000,2800,' \
            f'0000,{_w[:4]},{_w[4:]},{_h[:4]},{_h[4:]},0100,1800,0000,' \
            f'0000,4001,0000,7412,0000,7412,0000,0000,' \
            f'0000,0000,0000'.split(',')
    return _head


def pic_write(_path, _head, _new_data):
    with open(f'{_path}.bmp', 'ab+') as _f:
        _f.seek(0)
        _f.truncate()
        for _j in _head:
            if _j != '':
                _j = int(_j, 16)
                _bj = _j.to_bytes(2, 'big')
                _f.write(_bj)
        _f.write(_new_data)
    print('Done!')


def main():
    _path = input('输入绝对路径：').replace("'","")
    if _path[-1:] == ' ':
        _path = _path[:-1]
    print(_path)
    with open(_path, 'r') as _f:
        _data_encoded = _f.read().encode('utf-8')
    _w, _h = w_h_calc(_data_encoded)
    # 根据宽度，计算每行应多长，使其可以被4整除
    # 生成新的图像像素
    _new_data = ins_0(_w, _h, _data_encoded)
    # 图像大小
    _size = 54 + len(_new_data)
    _head = gen_head(_size, _w, _h)
    pic_write(_path, _head, _new_data)


if __name__ == '__main__':
    main()
