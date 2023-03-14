import string
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
spreadsheetID = '1UOOxF2GZFDZNJh56ggyPGrZDiqoR4AZHErOCV0dvatA'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'


service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=spreadsheetID, range="bot_practices!A2:A10").execute()
# delete = service.spreadsheets().values().clear(spreadsheetId=spreadsheetID, range="bot_matches!A2:C2", body={}).execute()

# request = sheet.values().update(spreadsheetId=spreadsheetID, range="bot_matches!A4", valueInputOption="USER_ENTERED", body={"values":[["Saratoga"]]}).execute()
# request = sheet.values().update(spreadsheetId=spreadsheetID, range="bot_matches!A3", valueInputOption="USER_ENTERED", body={"values":[["Lynbrook"]]}).execute()

                    
# values = (result.get('values', []))[0][0]
# result = result.get('values',[])
# print(result)

# practiceDays  =[]
# practices = sheet.values().get(spreadsheetId=spreadsheetID, range="bot_practices!A2:A10").execute()
# practices = practices.get('values',[])
# for i in practices:
#     practiceDays.append(str(i[0]).replace(" ", "").upper())

# active_status = sheet.values().get(spreadsheetId=spreadsheetID, range="bot_practices!D2").execute()
# active_status = active_status.get('values', [])[0][0]
# print(active_status)