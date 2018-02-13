import contextlib
import csv
import unittest
import os
import sys
import datetime

sys.path.append('../src/')
from writemetricscommand import *
from lightmetrics import *

class TestMetricsWriter(unittest.TestCase):

    def setup():
        with contextlib.suppress(FileNotFoundError):
            os.remove('metrics.csv')

    def test_column_readers_are_written_correctly(self):
        cut = WriteMetricsCommand('metrics.csv')
        lightmetrics = LightMetrics(datetime.date, datetime.time, '1', 1)
        cut.writeheader(lightmetrics)

        with open('metrics.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            lines = list(reader)
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0], ['date', 'time', 'roomnumber', 'islighton'])


if __name__ == '__main__':
    unittest.main()
