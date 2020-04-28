# def tree(dic, que=list()):

#     for k, v in dic.items():

#         if type(v) is dict:
#             que.append(v)
#             values = [val for val in v.keys()]
#             print(f'{k}: {values}')
#         else:
#             print(f'{k}: [{v}]')

#     while que:
#         new_dic = que.pop(0)
#         tree(new_dic, que)


def times_two(x):
    return x * 2


def deep_find(data, key):

    result = 'control value'

    for k, v in data.items():
        if result != 'control value':
            break

        elif k is key:
            result = v

        elif type(v) is dict:
            result = deep_find(v, key)

    return result


def broad_find(dic, key, que=list()):

    result = 'control value'

    for k, v in dic.items():

        if k is key:
            result = v
            return result

        elif type(v) is dict:
            que.append(v)

    while que:
        new_dic = que.pop(0)
        result = broad_find(new_dic, key, que)

        if result != 'control value':
            return result


def deep_f_all(data, key):

    for k, v in data.items():

        if k is key:
            yield v

        if type(v) is dict:
            yield from deep_f_all(v, key)


def broad_f_all(dic, key, que=list()):

    for k, v in dic.items():

        if k is key:
            yield v

        if type(v) is dict:
            que.append(v)

    while que:
        new_dic = que.pop(0)
        yield from broad_f_all(new_dic, key, que)


def deep_update(data, key, val):

    for k, v in data.items():

        if k is key:
            data[k] = val

        elif type(v) is dict:
            data[k] = deep_update(v, key, val)

    return data


def deep_apply(func, data):

    for k, v in data.items():

        try:

            if type(v) is dict:
                data[k] = deep_apply(func, v)
            else:
                data[k] = func(v)

        except TypeError as T:
            pass
            # print(f'Couldn\'t run {func.__name__} on {k}: {v}, because of\n{T}\n')

    return data


def deep_compare(obj1, obj2):
    return obj1 == obj2
    #  Is this it? What am I missing?


def flatten_sch(sch):

    for item in sch:

        if type(item) is not list:
            yield item
        else:
            yield from flatten_sch(item)


def flatten_dic(dic):

    for k, v in dic.items():
        yield k

        if type(v) is dict:
            yield from flatten_dic(v)


def schema_validator(schema=list(), data=dict()):

    flat_sch = [s for s in flatten_sch(schema)]
    flat_dic = [d for d in flatten_dic(data)]

    return flat_sch == flat_dic
