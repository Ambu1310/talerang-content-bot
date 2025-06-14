import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials
creds_dict = json.loads(os.getenv("GOOGLE_CREDS"))
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(credentials)

# Replace with your sheet ID
SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
SHEET_NAME = "Sheet1"

def save_to_sheet(week, audience, trend, post):
    sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    sheet.append_row([week, audience, trend, post])
