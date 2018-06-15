def add(matrix1, matrix2):
    # This is not idiomatic at all
    # Does not pass bonuses
    new_matrix = []
    if len(matrix1) != len(matrix2):
        raise ValueError("Matrices are not the same shape")
    for i, inner_list in enumerate(matrix1):
        if len(inner_list) != len(matrix2[i]):
            raise ValueError("Matrices are not the same shape")
        new_inner = []
        for j, element in enumerate(inner_list):
            new_inner.append(element + matrix2[i][j])
        new_matrix.append(new_inner)
    return new_matrix
