import requests
def Weather(city):
    API_key = "09912881a55e4c1570007a3256ab9d73"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    print("Final Url", weather_data)
    return weather_data['main']
