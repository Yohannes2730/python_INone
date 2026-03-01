import requests

API_KEY = "e725fb0a83c419bf733278c4ad836a02"

def temperature_advisor(temp):
    if temp < 10:
        return "It's very cold. Wear a heavy jacket."
    elif temp <= 20:
        return "It's cool. Wear a light jacket."
    elif temp <= 30:
        return "Nice weather. A T-shirt is fine."
    else:
        return "It's hot! Stay hydrated."

try:
    location_data = requests.get("https://ipinfo.io/json").json()

    city = location_data.get("city")

    if city is None:
        print("Cannot detect location.")
        exit()

    print("Detected Location:", city)

    # Get weather data
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        print("*********************************************")
        print("City:", city)
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {description}")
        print("Advice:", temperature_advisor(temperature))
        print("*********************************************")

    else:
        print("Weather fetch error:", data.get("message"))

except Exception as e:
    print("Connection error:", e)