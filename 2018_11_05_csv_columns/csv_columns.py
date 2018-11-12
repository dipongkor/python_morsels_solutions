
from collections import OrderedDict

import pandas as pd


def csv_columns(file, headers=None, missing=None):
    """Get an OrderedDict representation of a CSV file.

    Args:
        file: A file object with CSV data
        headers: Column labels to use.  If None, the first row of the
            file is used.
        missing: Value that should be used for null values

    Returns:
        An OrderedDict
    """
    if headers:
        df = pd.read_csv(file, dtype=str, names=headers)
    else:
        df = pd.read_csv(file, dtype=str)
    df = df.where(df.notnull(), missing)  # Replace NaN values

    columns = list(df.columns.values)
    d = OrderedDict()
    for col in columns:
        print(col)
        d[col] = list(df[col])
    return d


if __name__ == "__main__":
    with open("demo.csv", "r") as file:
        d = csv_columns(file)
