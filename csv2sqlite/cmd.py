import argparse

from csv2sqlite.db import CSVDatabase
from csv2sqlite.utils import parse_csv


def main():
    parser = argparse.ArgumentParser(
        description='CLI application that reads and saves a CSV file to a SQLite database.')
    parser.add_argument(
        'csvfile',
        type=argparse.FileType('r'),
        help='A CSV file to read from.')
    parser.add_argument(
        '--rows',
        type=int,
        help='Number of rows to process per iteration in case the file is too big. Default none.')
    parser.add_argument(
        '--delimiter',
        type=str,
        help='Character that separates the different fields in the CSV. Default \',\''
    )
    parser.add_argument(
        '--database',
        type=str,
        help='SQLite database file location. Default db/csv2sqlite.db'
    )

    args = parser.parse_args()

    if args.delimiter is None:
        file_iterator = parse_csv(args.csvfile, args.rows)
    else:
        file_iterator = parse_csv(args.csvfile, args.rows, args.delimiter)

    table_name = args.csvfile.name

    if args.database is None:
        db = CSVDatabase()
    else:
        db = CSVDatabase(args.database)

    db.save_csv(file_iterator, table_name)


if __name__ == '__main__':
    main()
