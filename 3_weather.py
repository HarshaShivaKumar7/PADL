import csv
import random
import requests

# Function to create synthetic weather details in a CSV file
def create_synthetic_weather_data(filename):
    places = [
        {"name": "New York", "country": "US", "lat": 40.7128, "lon": -74.0060},
        {"name": "London", "country": "GB", "lat": 51.5074, "lon": -0.1278},
        {"name": "Tokyo", "country": "JP", "lat": 35.6895, "lon": 139.6917},
        {"name": "Sydney", "country": "AU", "lat": -33.8688, "lon": 151.2093}
    ]
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "country", "lat", "lon", "weather", "description", "temp"])
        
        for place in places:
            weather = random.choice(["Clear", "Clouds", "Rain", "Snow"])
            description = random.choice(["clear sky", "few clouds", "scattered clouds", "light rain", "moderate rain", "heavy snow", "light snow"])
            temp = round(random.uniform(-10, 35), 2)
            
            writer.writerow([place["name"], place["country"], place["lat"], place["lon"], weather, description, temp])

# Function to load the CSV file data into a dictionary
def load_weather_data(filename):
    weather_data = {}
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            place_name = row["name"]
            weather_data[place_name] = row
            
    return weather_data

# Function to display weather details based on place name
def display_weather_by_place(weather_data, place_name):
    if place_name in weather_data:
        data = weather_data[place_name]
        print(f"Place: {data['name']}, {data['country']}")
        print(f"Weather: {data['weather']} ({data['description']})")
        print(f"Temperature: {data['temp']}°C")
    else:
        print("Place not found.")

# Function to display weather details based on latitude and longitude
def display_weather_by_coordinates(lat, lon, weather_data):
    for place, data in weather_data.items():
        if float(data["lat"]) == lat and float(data["lon"]) == lon:
            print(f"Place: {data['name']}, {data['country']}")
            print(f"Weather: {data['weather']} ({data['description']})")
            print(f"Temperature: {data['temp']}°C")
            return
    print("Coordinates not found in synthetic data. Fetching real-time data...")

    # Fetch real-time data from OpenWeatherMap API if coordinates are not in synthetic data
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=3118cd38ee3c8d85bea678b7100a9d31&units=metric"
    data = requests.get(url).json()
    
    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return
    
    weather_info = data['weather'][0]
    main_info = data['main']
    print(f"Place: {data['name']}, {data['sys']['country']}")
    print(f"Weather: {weather_info['main']} ({weather_info['description']})")
    print(f"Temperature: {main_info['temp']}°C")

if __name__ == "__main__":
    filename = "synthetic_weather_data.csv"
    create_synthetic_weather_data(filename)
    weather_data = load_weather_data(filename)
    
    while True:
        choice = input("Enter '1' to search by place name or '2' to search by coordinates: ")
        if choice == '1':
            place_name = input("Enter place name: ")
            display_weather_by_place(weather_data, place_name)
        elif choice == '2':
            lat = float(input("Enter latitude: "))
            lon = float(input("Enter longitude: "))
            display_weather_by_coordinates(lat, lon, weather_data)
        else:
            print("Invalid choice. Please enter '1' or '2'.")
