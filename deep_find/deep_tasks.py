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
#         nd = que.pop(0)
#         tree(nd, que)


def df_dfs(data, key):

    result = 'control value'

    for k, v in data.items():
        if result != 'control value':
            break

        elif k is key:
            result = v

        elif type(v) is dict:
            result = df_dfs(v, key)

    return result


def df_bfs(dic, key, que=list()):

    result = 'control value'

    for k, v in dic.items():

        if k is key:
            result = v
            return result

        elif type(v) is dict:
            que.append(v)

    while que:
        new_dic = que.pop(0)
        result = df_bfs(new_dic, key, que)

        if result != 'control value':
            return result
