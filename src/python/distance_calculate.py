#!/usr/bin/env python3
import json
import sys


class DistanceCalculator():
    _User_Data = []
    _Name = []
    _Name_2 = []
    _Name_Count = []
    _Name_Count_2 = []
    _Name_Metaphone = []
    _Name_Metaphone_2 = []
    _Index_counter = []
    _Output_File_Name = r"D:\buet-ict\ai-term-paper\Countrynameproject\temp\distance_calculated_data.json"
    _connection_file = r"D:\buet-ict\ai-term-paper\Countrynameproject\temp\clustered_data.json"
    _levenshtein_Value = int

    def read(self):
        connection_file = open(self._connection_file, 'r')
        try:
            qByUser = connection_file.read()
            self._User_Data = json.loads(qByUser)
        except ValueError:
            print
            'Decoding JSON has failed'
        connection_file.close()
        Distance_Calculator.divide()

    def divide(self):
        _list = list(self._User_Data.values())
        # print(_list)
        for index, val in enumerate(self._User_Data):
            self._Name.append(val)
            self._Name_Count.append(_list[index][0])
            self._Name_Metaphone.append(_list[index][1])

        with open(self._Output_File_Name, 'w') as outfile:
            json.dump(self._User_Data, outfile, indent=4)
        Distance_Calculator.compare()

    def compare(self):
        for index_1, value_1 in enumerate(self._Name_Metaphone):
            for index_2, value_2 in enumerate(self._Name_Metaphone):
                if value_1 == value_2:
                    # print(str(index_2) +" "+ str(value_2))
                    self._Index_counter.append(index_2)

            if len(self._Index_counter) != 0:
                Distance_Calculator.move(self._Index_counter)

    def move(self, indexCounter):
        for value_3 in indexCounter:
            # print(str(value_3) + " " +str(len(self._Name_Metaphone)))
            self._Name_2.append(self._Name[value_3])
            self._Name_Count_2.append(self._Name_Count[value_3])
            self._Name_Metaphone_2.append(self._Name_Metaphone[value_3])
        for value in sorted(indexCounter, reverse=True):
            del self._Name_Metaphone[value]
            del self._Name[value]
            del self._Name_Count[value]

        self._Index_counter.clear()
        Distance_Calculator.compare()

    def Dumping(self):
        To_Add = dict(zip(self._Name_2, self._Name_Metaphone_2))
        c = 0
        for key, val in To_Add.items():
            To_Add[key] = [self._Name_Count_2[c], To_Add[key]]
            c += 1

        print(To_Add)
        # print(self._Name_2[index])
        # _user_data_2[index]={self._Name_Count_2[index],self._Name_Metaphone_2[index]}
        # val=self._Name_2[index]
        # self._User_Data[val][0]=self._Name_Count_2[index]
        # self._User_Data[val][1]=self._Name_Metaphone_2[index]

        # print(self._User_Data[0])
        with open(self._Output_File_Name, 'w') as outfile:
            json.dump(To_Add, outfile, indent=4)


if __name__ == '__main__':
    Distance_Calculator = DistanceCalculator()
    Distance_Calculator.read()
    Distance_Calculator.Dumping()
