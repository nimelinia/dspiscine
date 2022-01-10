def data_type():
    int_ = 1
    str_ = 'hello'
    float_ = 3.14
    bool_ = False
    list_ = []
    dict_ = {'hello': 'world'}
    tuple_ = (int_, str_)
    set_ = set()
    print('[', end='')
    print(type(int_).__name__, end=', ')
    print(type(str_).__name__, end=', ')
    print(type(float_).__name__, end=', ')
    print(type(bool_).__name__, end=', ')
    print(type(list_).__name__, end=', ')
    print(type(dict_).__name__, end=', ')
    print(type(tuple_).__name__, end=', ')
    print(type(set_).__name__, end=']')


if __name__ == '__main__':
    data_type()