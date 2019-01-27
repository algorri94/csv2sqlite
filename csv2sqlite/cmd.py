import argparse

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

args = parser.parse_args()