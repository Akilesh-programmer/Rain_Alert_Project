import requests
from twilio.rest import Client

API_KEY = "2c7bcfa610522b31c086d210fa3ae06f"
MY_LAT = -26.204103
MY_LNG = 28.047304
ACCOUNT_SID = "ACda535cb235918e420d29b42c7deb39e8"
AUTH_TOKEN = "581212ee28b1d664aa9dee11766cac39"

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LNG}&exclude=current,minutely,daily&appid"
    f"=2c7bcfa610522b31c086d210fa3ae06f")
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]
twelve_hour_data = hourly_data[:12]


# print(hourly_data[0]["weather"][0]["id"])

def rain_check():
    for thing in twelve_hour_data:
        if thing["weather"][0]["id"] < 700:
            return True


if rain_check():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
                body="It is gonna rain, so take that umbrella.",
                from_="+19564462998",
                to="+916379276131",
                )
print(message.status)
