import csv
import inspect

class WriteMetricsCommand:
    def __init__(self, filepath):
        self.__filepath = filepath

    def writeheader(self, metricsdefinition):
        with open(self.__filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow()
