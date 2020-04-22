def deep_find_dfs(data, key):

    for datum in data:

        if datum is key:
            return data[datum]

        if type(data[datum]) is dict:

            attempt = deep_find_dfs(data[datum], key)
            if attempt is not None:

                return attempt
