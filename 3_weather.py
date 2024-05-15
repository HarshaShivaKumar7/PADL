from faker import Faker
import random
import csv

def generate_weather():
	fake = Faker()
	
	with open('weather.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['place','temparature', 'humidity','weather'])
		for _ in range(100000):
			writer.writerow([fake.city(), round(random.uniform(-20, 40)),round(random.uniform(0, 100)),random.choice(['Sunny', 'Cloudy', 'Rainy', 'Snowy'])])


def load_data():
	with open('weather.csv', 'r') as file:
		reader=csv.reader(file)
		next(reader)
		return list(reader)


def weather_data(weather_list,city):
	
	for weather in weather_list:
		if weather[0] == city:
			print(f" \nCity : {weather[0]} \n Temperature :{weather[1]} C \n Humidity : {weather[2]} \n Weather : {weather[3]}")
			break

		


def menu():
	weather_list=load_data()

	while True:
		city = input("Enter city name : ")
		weather_data(weather_list,city)



if __name__ == "__main__":
	generate_weather()
	menu()
