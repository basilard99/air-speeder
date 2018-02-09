import contextlib
import csv
import unittest
import os
import sys

sys.path.append('../src/')
from writemetricscommand import *

class TestMetricsWriter(unittest.TestCase):

    def setup():
        with contextlib.suppress(FileNotFoundError):
            os.remove('metrics.csv')

    def test_column_readers_are_written_correctly(self):
        cut = WriteMetricsCommand('metrics.csv')
        cut.writeheader()

        with open('metrics.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            linecount = sum(1 for line in reader)
            self.assertEqual(linecount, 1)


if __name__ == '__main__':
    unittest.main()
