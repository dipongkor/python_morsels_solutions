def matrix_from_string(matrix_str):
    """Takes a string representing a 2D matrix where
    rows are delimited by newline characters and
    returns a list of lists
    """
    return [
        [float(element) for element in row.split()]
        for row in matrix_str.splitlines()
        if row and not row.isspace()
    ]
