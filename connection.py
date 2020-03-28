import gspread
from oauth2client.service_account import ServiceAccountCredentials


def createConnection():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('Face Detection.json', scope)
    client = gspread.authorize(creds)

    return (client.open("Face Detection test").sheet1)
