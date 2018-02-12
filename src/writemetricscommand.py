import csv

class WriteMetricsCommand:
    def __init__(self, filepath):
        self.__filepath = filepath

    def getattributes(self, metricsdefinition):
        boring = dir(type('dummyObject', (object,), {}))
        return [item
                for item in inspect.getmembers(metricsdefinition)
                if item[0] not in boring]

    def writeheader(self, metricsdefinition):
        with open(self.__filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(metricsdefinition.__dict__.keys())
