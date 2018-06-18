from itertools import zip_longest


def add(*matrices):
    total = []
    all = zip_longest(*matrices)
    for matching_columns in all:
        new_column = []
        try:
            matching_elements_tups = zip_longest(*matching_columns)
        except TypeError:
            raise ValueError("Matrices are different shapes")
        for elements_tup in matching_elements_tups:
            sum = 0
            for element in elements_tup:
                try:
                    sum += element
                except TypeError:
                    # This will get raised if matrices don't match in shape
                    raise ValueError("Matrices are different shapes")
            new_column.append(sum)
        total.append(new_column)
    return total
