# pylint: disable=all

'''
References:
https://developers.google.com/sheets/api/guides/concepts
https://developers.google.com/sheets/api/reference/rest
https://console.cloud.google.com/iam-admin/serviceaccounts/details/109707854910534239726?project=ryeeshu
https://developers.google.com/identity/protocols/oauth2/service-account#python

'''





# from __future__ import print_function

# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '138K6l-Z_gsva38rQHpHxcx8Z5zo9CbQ_Hrwm8WrbDco'
SAMPLE_RANGE_NAME = 'Sheet1!A1:D9'
SAMPLE_RANGE_NAME2 = 'Sheet2!B2'


# def main():
"""Shows basic usage of the Sheets API.
Prints values from a sample spreadsheet.
"""

# # The file token.json stores the user's access and refresh tokens, and is
# # created automatically when the authorization flow completes for the first
# # time.
# if os.path.exists('token.json'):
#     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# # If there are no (valid) credentials available, let the user log in.
# if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#         creds.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             'credentials.json', SCOPES)
#         creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open('token.json', 'w') as token:
#         token.write(creds.to_json())

# try:
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()

# if there are alues, get the values, otherwise get empty list
values = result.get('values', [])
print(values)

lst = [['aaa', 1, 11], ['bbb', 2, 22], ['ccc', 3, 33],]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME2, valueInputOption="USER_ENTERED", body={"values":lst}).execute()
print(request)


# if not values:
#     print('No data found.')
#     return

# print('Name, Major:')
# for row in values:
#     # Print columns A and E, which correspond to indices 0 and 4.
#     print('%s, %s' % (row[0], row[4]))
# except HttpError as err:
# print(err)


# if __name__ == '__main__':
#     main()