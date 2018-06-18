def matrix_from_string(mat_str):
    """Takes a string representing a matrix where
    rows are delimited by newline characters and
    returns a list of lists
    """
    matrix = []
    for col_str in mat_str.split("\n"):
        col = [float(x) for x in col_str.split()]
        if col:
            matrix.append(col)
    return matrix
