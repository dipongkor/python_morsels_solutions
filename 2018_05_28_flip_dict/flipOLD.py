def flip_dict_of_lists(d):
    flipped = {}
    for key, val_list in d.items():
        for val in val_list:
            try:
                flipped[val].append(key)
            except KeyError:
                flipped[val] = [key]
    return flipped
