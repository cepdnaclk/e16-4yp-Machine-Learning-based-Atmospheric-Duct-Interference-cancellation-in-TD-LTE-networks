import requests
import json
from geopy.geocoders import Nominatim
from datetime import date

def showWeather(city_name):
 
#Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "eef4adf69af7cfbd30dbb1c2b6f56357"  #sample API
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json() 
 
    return(weather_info['main'])   #to insert or send value in our Text Field to display output
    
       
def getCity(lat,lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(lat+","+lon)
    #print(location.raw['address']['city'])
    return(location.raw['address']['city'])



def getWheather(lat,lon):

    # city = getCity(lat,lon)
    # data = showWeather(city)
    api_key = "eef4adf69af7cfbd30dbb1c2b6f56357"
    url = "https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    weather_info = response.json() 
    #data = json.loads(response.text)
    today = date.today()
    for data in weather_info['list']:
        if str(today) in str(data['dt_txt']):
            return data