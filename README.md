# 🔗 API Automation & Integration Portfolio

A collection of API-based automation scripts and workflows for real-world use cases — from weather alerts and Slack command logging to GitHub Actions triggering external APIs. These projects demonstrate how to integrate Python and GitHub Actions with third-party APIs like OpenWeatherMap, Twilio, Google Sheets, and external webhook endpoints.

---

## Projects Included

### 1.  `weather-alerts-to-sms.py`

**Use Case**: Get real-time weather alerts via SMS using OpenWeatherMap and Twilio.

**Features**:
- Monitors severe weather conditions in your area
- Sends SMS notifications using Twilio
- Runs continuously with periodic checks (every 5 minutes)
- Tracks which alerts have been sent to avoid duplicates

**Technologies**:
- Python, Twilio API, OpenWeatherMap API, dotenv

**Setup**:
1. Create a `.env` file with the following keys:
    ```env
    OWM_API_KEY=your_openweather_api_key
    TWILIO_SID=your_twilio_sid
    TWILIO_AUTH=your_twilio_auth_token
    TWILIO_FROM=+1234567890
    ALERT_TO=+1987654321
    LAT=43.0731
    LON=-89.4012
    ```
2. Run the script:
    ```bash
    python weather-alerts-to-sms.py
    ```

---

### 2.  `slack-to-google-sheets.py`

**Use Case**: Log Slack slash command responses into a Google Sheet.

**Features**:
- Listens for POST requests from Slack slash commands
- Appends user input to a Google Sheet with a timestamp
- Uses a service account to authenticate with the Google Sheets API

**Technologies**:
- Python (Flask), Google Sheets API, Slack

**Setup**:
1. Set up a Google Cloud service account and download `credentials.json`.
2. Share the sheet with the service account email.
3. Replace `SHEET_ID` in the script.
4. Deploy the Flask app and point your Slack slash command to `https://yourserver.com/slack/command`.

---

### 3.  `github-webhook-alert.yml`

**Use Case**: GitHub Actions workflow that sends alerts to an external API based on workflow inputs and API-matched users.

**Features**:
- Triggered manually with `workflow_dispatch`
- Retrieves user data from an external API
- Matches emails against an on-call list stored as a secret
- Sends a POST request with the matched user’s ID to a target API
- Uses cURL, jq, and GitHub Actions environment secrets

**Technologies**:
- GitHub Actions, Bash, cURL, jq, REST APIs

**Setup**:
1. Add the following secrets to your GitHub repo:
    - `EXTERNAL_API_SERVER`
    - `EXTERNAL_API_KEY`
    - `ON_CALL_EMAILS_LIST` (comma-separated list)
    - `EXTERNAL_TARGET_API_URL`
    - `EXTERNAL_TARGET_API_KEY`
2. Trigger the workflow from the Actions tab with `callerId` and optional `message`.

