#!/usr/bin/env python3

import json
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GooglesheetReader(object):
    _scope = ['https://spreadsheets.google.com/feeds',
              'https://www.googleapis.com/auth/drive']
    _cred =  r"F:\Countrynameproject-master\src\conf\credential.json"
    _gsheet = 'Country name project'
    _outputfilename = r"F:\Countrynameproject-master\temp\data_from_googlesheets.json"

    def read(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(self._cred, self._scope)
        client = gspread.authorize(creds)
        sh = client.open(self._gsheet).get_worksheet(0)
        result = sh.col_values(1)

        with open(self._outputfilename, 'w') as outfile:
            json.dump(result, outfile)


if __name__ == '__main__':
    sheet_reader = GooglesheetReader()
    sheet_reader.read()
