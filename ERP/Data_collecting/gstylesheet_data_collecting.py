# from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

#   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#   pip install --upgrade httplib2

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1w_6nZwXFh1xOL-6-A532vjdWjhm1lVzp_Y5MVeEYw4U'

spreadsheet_id_costs = '1TU4lBUeTZDXjFzo8TBOr5HF5eaeY3g76q11QoJXP-uE'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)



# Example of filr reading
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range="DashBoard!D1:H7",
    majorDimension='ROWS'
).execute()

val = values['values']

# print(val)

print(val[2])
result = ''
for el in val[2]:
    if int(el)>=int(val[2][0]):
        result = "green"
    if int(el)<int(val[2][0]):
        result = "red"

    print(f"{el}-{result}")
