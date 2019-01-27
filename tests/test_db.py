from io import StringIO
import unittest
from pandas.io.parsers import TextFileReader
from csv2sqlite.db import CSVDatabase


class TestDB(unittest.TestCase):

    def test_db_save_csv(self):
        db = CSVDatabase('')
        file_iterator = TextFileReader(StringIO('a,b,c\n1,2,3'))
        db.save_csv(file_iterator, 'test')
        result = db.engine.execute('SELECT a,b,c FROM test')
        result = result.first()
        self.assertEqual(result['a'], 1)
        self.assertEqual(result['b'], 2)
        self.assertEqual(result['c'], 3)


if __name__ == '__main__':
    unittest.main()
