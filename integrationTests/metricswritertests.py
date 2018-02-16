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

    def test_column_headers_are_written_correctly(self):
        cut = WriteMetricsCommand('metrics.csv')
        lightmetrics = LightMetrics(datetime.date, datetime.time, '1', 1)
        cut.writeheader(lightmetrics)

        with open('metrics.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            lines = list(reader)
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0], ['date', 'time', 'roomnumber', 'islighton'])

    def test_data_written_correctly(self):
        cut = WriteMetricsCommand('metrics.csv')
        lightmetrics1 = LightMetrics(datetime.date(2018, 1, 1), datetime.time(0, 0, 0), '1', True)
        lightmetrics2 = LightMetrics(datetime.date(2018, 1, 1), datetime.time(0, 0, 30), '1', False)
        lightmetrics3 = LightMetrics(datetime.date(2018, 1, 1), datetime.time(0, 1, 0), '1', True)
        lightmetrics4 = LightMetrics(datetime.date(2018, 1, 1), datetime.time(0, 1, 30), '1', False)

        cut.writeheader(lightmetrics1)
        cut.writedata(lightmetrics1)
        cut.writedata(lightmetrics2)
        cut.writedata(lightmetrics3)
        cut.writedata(lightmetrics4)

        with open('metrics.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            lines = list(reader)

        self.assertEqual(len(lines), 5)
        self.assertEqual(lines[0], ['date', 'time', 'roomnumber', 'islighton'])
        self.assertEqual(lines[1], ['2018-01-01', '00:00:00', '1', 'True'])
        self.assertEqual(lines[2], ['2018-01-01', '00:00:30', '1', 'False'])
        self.assertEqual(lines[3], ['2018-01-01', '00:01:00', '1', 'True'])
        self.assertEqual(lines[4], ['2018-01-01', '00:01:30', '1', 'False'])

if __name__ == '__main__':
    unittest.main()
