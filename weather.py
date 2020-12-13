import requests
from key import key
def Weather(city):
    API_key = key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    print("Final Url", weather_data)
    return weather_data['main']


