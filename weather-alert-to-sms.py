import requests
import time
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Load environment variables
OWM_API_KEY = os.getenv("OWM_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_FROM = os.getenv("TWILIO_FROM")
ALERT_TO = os.getenv("ALERT_TO")
LAT = os.getenv("LAT")
LON = os.getenv("LON")

# Initialize Twilio client
client = Client(TWILIO_SID, TWILIO_AUTH)

# Track last alert sent
last_alert_sent = set()

def get_weather_alerts():
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LON}&appid={OWM_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("alerts", [])

def send_sms_alert(alert):
    message = f"⚠️ Weather Alert: {alert['event']}\n{alert['description'][:200]}...\nExpires: {alert['end']}"
    client.messages.create(
        to=ALERT_TO,
        from_=TWILIO_FROM,
        body=message
    )
    print(f"Sent alert: {alert['event']}")

def check_and_alert():
    global last_alert_sent
    alerts = get_weather_alerts()
    for alert in alerts:
        alert_id = alert["event"] + str(alert["start"])
        if alert_id not in last_alert_sent:
            send_sms_alert(alert)
            last_alert_sent.add(alert_id)

if __name__ == "__main__":
    print("🌦️ Starting weather alert service...")
    while True:
        try:
            check_and_alert()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(300)  # Check every 5 minutes
