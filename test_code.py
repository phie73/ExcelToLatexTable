import unittest
from helpfun import *

class TestCases(unittest.TestCase):
    def test_filepath(self):
        self.assertEqual(filepath(None, '/users/sophia/home/something/herenot', 0), '/users/sophia/home/something/table.tex')
    def test_filepath_2(self):
        self.assertEqual(filepath('/users/sophia/home/something/table.tex', '/users/sophia/home/something/herenot', 0), '/users/sophia/home/something/table.tex')
    def test_filepath_3(self):
        self.assertEqual(filepath(None, '/users/sophia/home/something/herenot', 1), '/users/sophia/home/something/csvfile.csv')
    def test_filepath_4(self):
        self.assertEqual(filepath(None, '/users/sophia/home/something/herenot', 3), -1)
    def test_numcsv_1(self):
        self.assertEqual(col_csv('/home/sophia/ExcelToLatexTable/csvfile.csv'), 5)

if __name__ == '__main__':
    unittest.main()
