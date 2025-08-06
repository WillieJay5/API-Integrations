from flask import Flask, request, jsonify
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
import os

app = Flask(__name__)

# Google Sheets setup
SHEET_ID = 'YOUR_SHEET_ID_HERE'
SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
sheets = build('sheets', 'v4', credentials=credentials)

@app.route('/slack/command', methods=['POST'])
def handle_slash_command():
    user = request.form.get('user_name')
    text = request.form.get('text')
    channel = request.form.get('channel_name')
    timestamp = datetime.datetime.now().isoformat()

    # Add to Google Sheets
    sheets.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range="A:D",
        valueInputOption="USER_ENTERED",
        body={"values": [[timestamp, user, channel, text]]}
    ).execute()

    return jsonify({
        "response_type": "ephemeral",
        "text": f"Thanks, {user}! Your response has been logged."
    })

if __name__ == '__main__':
    app.run(port=3000)
