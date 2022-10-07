#!/usr/bin/env python3

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GooglesheetWritter():
    _User_Data = []
    _Name = []
    _Name_Count = []
    _Name_Metaphone = []
    _Unique_Metaphone = []
    count = 1
    _temp_val = []
    _temp_key = []
    _scope = ['https://spreadsheets.google.com/feeds',
              'https://www.googleapis.com/auth/drive']
    _cred = r"D:\buet-ict\ai-term-paper\Countrynameproject\src\conf\credential.json"
    _gsheet = 'Country name project'
    _inputfilename = r"D:\buet-ict\ai-term-paper\Countrynameproject\temp\distance_calculated_data.json"

    def read(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(self._cred, self._scope)
        client = gspread.authorize(creds)
        sh = client.open(self._gsheet).get_worksheet(1)
        cell_list0 = sh.range('A2:A5000')
        cell_list1 = sh.range('B2:B5000')
        cell_list2 = sh.range('C2:C5000')
        cell_list3 = sh.range('D2:D5000')
        connection_file = open(self._inputfilename, 'r')
        try:
            qByUser = connection_file.read()
            self._User_Data = json.loads(qByUser)
        except ValueError:
            print
            'Decoding JSON has failed'
        connection_file.close()
        _list = list(self._User_Data.values())
        value = str(_list[0][1])

        for index, val in enumerate(self._User_Data):
            if value != str(_list[index][1]):
                self.count += 1
                value = str(_list[index][1])
            self._Unique_Metaphone.append(self.count)
            self._Name.append(val)
            self._Name_Count.append(_list[index][0])
            self._Name_Metaphone.append(_list[index][1])

        for i, val in enumerate(self._Name):
            cell_list2[i].value = self._Name[i]
            cell_list3[i].value = self._Name_Count[i]
            cell_list1[i].value = self._Name_Metaphone[i]
            cell_list0[i].value = self._Unique_Metaphone[i]
        sh.update_cells(cell_list0)
        sh.update_cells(cell_list1)
        sh.update_cells(cell_list2)
        sh.update_cells(cell_list3)


if __name__ == '__main__':
    Googlesheet_Writter = GooglesheetWritter()
    Googlesheet_Writter.read()
