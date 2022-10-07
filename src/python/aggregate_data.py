#!/usr/bin/env python3

import json
from collections import defaultdict


class DataAggregator(object):
    _User_Data = []
    _connection_file = r"D:\buet-ict\ai-term-paper\Countrynameproject\temp\data_from_googlesheets.json"
    _outputfilename = r"D:\buet-ict\ai-term-paper\Countrynameproject\temp\aggregated_data.json"

    def read(self):
        connection_file = open(self._connection_file, 'r')
        try:
            qByUser = connection_file.read()
            self._User_Data = json.loads(qByUser)
        except ValueError:
            print
            'Decoding JSON has failed'
        connection_file.close()

    def write(self):
        with open(self._outputfilename, 'w') as outfile:
            json.dump(sortDic, outfile, indent=4)

    def get_cnt(self, lVals):
        d = defaultdict(int)
        for x in lVals:
            d[x] += 1

        return d


if __name__ == '__main__':
    Data_Aggregator = DataAggregator()
    Data_Aggregator.read()
    sortDic = dict(sorted(Data_Aggregator.get_cnt(Data_Aggregator._User_Data).items()))
    Data_Aggregator.write()
