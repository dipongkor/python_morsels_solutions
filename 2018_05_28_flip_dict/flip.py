def flip_dict_of_lists(d, **kwargs):
    flipped = {}
    if 'dict_type' in kwargs:
        flipped = kwargs['dict_type'](flipped)
    for key, val_list in d.items():
        for val in val_list:
            if 'key_func' in kwargs:
                val = kwargs['key_func'](val)
            try:
                flipped[val].append(key)
            except KeyError:
                flipped[val] = [key]
    return flipped
