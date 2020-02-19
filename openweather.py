

#openweather_api key = 1dfdaa0233fae87f58e47ba2796f12d3

import requests
from pprint import pprint
import json


hostname = 'http://api.openweathermap.org'
resource = '/data/2.5/weather'
url = hostname + resource + '?q=Halifax&units=metric&appid=1dfdaa0233fae87f58e47ba2796f12d3'
response = requests.get(url)
print(response)
weather = response.json()
print(type(weather))
weather_str = json.dumps(weather, indent=2) # json dumps use for converting string
#print(weather_str)
#print(weather["main"]["temp"])
print(weather["weather"][0]["description"])
#print(weather["clouds"]["all"])


cred = {"username": "sagor.ghosh@dal.ca", "password": "December@25"}
url = 'http://api.openweathermap.org'
ticket_url



