import os

from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build


KEY = "AIzaSyCU8AOyOFfPBH5aZnphqXhg6aeD6dix0nk"
SHEET_ID = "1BuG9Hn0S7r-8KmtKMawUCq2tonhNEbWKIJ4Y-u8IhGo"

app = Flask(__name__)

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open("yuqing@coronasmittetinorge.iam.gserviceaccount.com").sheet1
data = sheet.get_all_records()
labels = []
locations = []
for row in data:
    labels.append(row['label'])


@app.route('/')
def index():
    return render_template("index.html", labels=labels)


@app.route('/google3c8d8110329b8523.html')
def google_search_verify():
    return render_template("google3c8d8110329b8523.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)