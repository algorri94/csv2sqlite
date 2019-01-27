import unittest
from io import StringIO
from csv2sqlite.utils import parse_csv


class TestUtils(unittest.TestCase):

    def test_read_csv(self):
        file = StringIO('a,b,c\n1,2,3')
        file_iterator = parse_csv(file)
        chunk = file_iterator.get_chunk(1)
        self.assertEqual(['a', 'b', 'c'], list(chunk.columns.values))
        self.assertEqual(chunk.iloc[0]['a'], 1)
        self.assertEqual(chunk.iloc[0]['b'], 2)
        self.assertEqual(chunk.iloc[0]['c'], 3)

    def test_read_csv_delimiter(self):
        file = StringIO('a;b;c\n1;2;3')
        file_iterator = parse_csv(file, delimiter=';')
        chunk = file_iterator.get_chunk(1)
        self.assertEqual(['a', 'b', 'c'], list(chunk.columns.values))
        self.assertEqual(chunk.iloc[0]['a'], 1)
        self.assertEqual(chunk.iloc[0]['b'], 2)
        self.assertEqual(chunk.iloc[0]['c'], 3)

    def test_read_csv_chunks(self):
        file = StringIO('a,b,c\n1,2,3\n4,5,6')
        file_iterator = parse_csv(file, rows=1)
        chunk = file_iterator.get_chunk(1)
        self.assertEqual(['a', 'b', 'c'], list(chunk.columns.values))
        self.assertEqual(chunk.iloc[0]['a'], 1)
        self.assertEqual(chunk.iloc[0]['b'], 2)
        self.assertEqual(chunk.iloc[0]['c'], 3)
        chunk = file_iterator.get_chunk(2)
        self.assertEqual(chunk.iloc[0]['a'], 4)
        self.assertEqual(chunk.iloc[0]['b'], 5)
        self.assertEqual(chunk.iloc[0]['c'], 6)


if __name__ == '__main__':
    unittest.main()
