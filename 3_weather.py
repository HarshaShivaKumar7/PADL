import requests

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=3118cd38ee3c8d85bea678b7100a9d31&units=metric"
    data = requests.get(url).json()
    
    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return
    
    weather_info = data['weather'][0]  # Extracts the weather information from the response
    main_info = data['main']  # Extracts the main temperature and other related information

    print(f"Place: {data['name']}, {data['sys']['country']}")
    print(f"Weather: {weather_info['main']} ({weather_info['description']})")
    print(f"Temperature: {main_info['temp']}°C")

if __name__ == "__main__":
    while True:
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))
        get_weather(latitude, longitude)
