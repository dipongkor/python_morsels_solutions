def matrix_from_string(mat_str):
    matrix = []
    for col_str in mat_str.split("\n"):
        col = [float(x) for x in col_str.split()]
        if col:
            matrix.append(col)
    return matrix
