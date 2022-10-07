#!/usr/bin/env python3

import json
from phonetics import metaphone


class DataCluster(object):
    _User_Data = []
    _Metaphone_User_Data = []
    _Output_File_Name = r"D:\buet-ict\ai-term-paper\Countrynameproject\temp\clustered_data.json"
    _connection_file = r"D:\buet-ict\ai-term-paper\Countrynameproject\temp\aggregated_data.json"

    def read(self):
        connection_file = open(self._connection_file, 'r')
        try:
            qByUser = connection_file.read()
            self._User_Data = json.loads(qByUser)
        except ValueError:
            print
            'Decoding JSON has failed'
        connection_file.close()

        for index, val in enumerate(self._User_Data):
            self._Metaphone_User_Data.append(metaphone(val))

        To_Add = dict(zip(self._User_Data, self._Metaphone_User_Data))

        for key, val in To_Add.items():
            if key in self._User_Data:
                print(val)
                self._User_Data[key] = [self._User_Data[key], val]

        with open(self._Output_File_Name, 'w') as outfile:
            json.dump(self._User_Data, outfile, indent=4)


if __name__ == '__main__':
    Data_Aggregator = DataCluster()
    Data_Aggregator.read()
