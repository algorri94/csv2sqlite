import pandas


def parse_csv(csv, rows=None, delimiter=','):
    return pandas.read_csv(csv, chunksize=rows, sep=delimiter, iterator=True)
