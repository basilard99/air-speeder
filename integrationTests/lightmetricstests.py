import contextlib
import csv
import unittest
import os
import sys
import datetime

sys.path.append('../src/')
from lightmetrics import *

class TestMetricsWriter(unittest.TestCase):

    def test_object_initialized_correctly(self):
        testdate = datetime.date(2018, 1, 1)
        testtime = datetime.time(5,15,32)
        testroomnumber = '1'
        testislighton = False
        cut = LightMetrics(testdate, testtime, testroomnumber, testislighton)
        self.assertEqual(cut.date, testdate)
        self.assertEqual(cut.time, testtime)
        self.assertEqual(cut.roomnumber, testroomnumber)
        self.assertEqual(cut.islighton, testislighton)

if __name__ == '__main__':
    unittest.main()
