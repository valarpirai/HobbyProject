import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

import datetime

from pageSpeedTest import *

secret_file = 'client_secret.json'
# json_key = json.load(open(secret_file))

# OAuth 2 Authorize
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(secret_file, scope)
client = gspread.authorize(credentials)

# Open Sheet
sheets = client.open('Identifor.com - Performance Improvement')
# Select fitst sheet
first_sheet = sheets.sheet1

#Create new Sheet
new_sheet_name = 'Pagespeed Score - ' + datetime.date.today().strftime('%B %d')

try:
    new_sheet = sheets.worksheet(new_sheet_name)
    print('Overwriting existing sheet: ' + new_sheet_name)
except gspread.exceptions.WorksheetNotFound as e:
    new_sheet = sheets.add_worksheet(title=new_sheet_name, rows='100', cols='5')
    print('Creating new sheet: ' + new_sheet_name)


page_names = first_sheet.col_values(1)
url_list = first_sheet.col_values(2)

# print(page_names)
# print(url_list)

print('Updating New Sheet: ' + new_sheet_name)
# Select a range
page_name_cells = new_sheet.range('A1:A' + str(len(page_names)))

index = 0;
for cell in page_name_cells:
    cell.value = page_names[index]
    index += 1

# Update in batch
new_sheet.update_cells(page_name_cells)

url_cells = new_sheet.range('B1:B' + str(len(url_list)))

new_sheet.update_acell('C1', 'Mobile Score')
new_sheet.update_acell('D1', 'Desktop Score')

tester = PageSpeedInsights()

index = 0;
for cell in url_cells:
    cell.value = url_list[index]
    
    if index > 0:
        mobile_score = tester.getPagespeedScore(url_list[index], 'mobile')
        desktop_score = tester.getPagespeedScore(url_list[index])

        print(str(index) + ' - ' + url_list[index] + ' : ' + str(mobile_score) + ' : ' + str(desktop_score))

        new_sheet.update_acell('C' + str(index + 1), str(mobile_score))
        new_sheet.update_acell('D' + str(index + 1), str(desktop_score))

    index += 1

    if index%10 == 0:
        print("Waiting for 30 seconds. Otherwise captcha will be asked.")
        time.sleep(30)

# Update in batch
new_sheet.update_cells(url_cells)

print('Page name, url, Mobile and desktop score are updated list are updated.')
