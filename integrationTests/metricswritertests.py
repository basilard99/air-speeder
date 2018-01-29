import unittest
import os

class TestMetricsWriter(unittest.TestCase):

    def test_fileExists(self):
        self.assertTrue(os.path.isfile('metrics.csv'))

if __name__ == '__main__':
    unittest.main()
