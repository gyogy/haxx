# import ipdb

diki = {
    'A': {
        'C': [2, 5],
        'D': {
            'I': 'heyo!',
            'J': 6,
            'F': 'In [A][D]'
        },
        'E': False
    },
    'B': {
        'F': 'In [B]',
        'G': None,
        'H': True
    }
}


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
