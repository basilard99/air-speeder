import unittest
import os
import sys

sys.path.append('../src/')
from writemetricscommand import *

class TestMetricsWriter(unittest.TestCase):

    def test_fileExists(self):
        x = WriteMetricsCommand('metrics.csv')
        self.assertTrue(os.path.isfile('metrics.csv'))

if __name__ == '__main__':
    unittest.main()
