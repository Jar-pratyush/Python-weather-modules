from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Mumbai"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

#We are writing the name here as in case the file is called directly then in order to execute in the terminal we need this:

if __name__== "__main__":
    print('\n*** Get Current Weather Condtions ***\n')
    city = input("\nPlease enter a city name:")

    #Check for empty strings or strings with only spaces:
    if not bool(city.strip()):
        city = "Mumbai"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)

