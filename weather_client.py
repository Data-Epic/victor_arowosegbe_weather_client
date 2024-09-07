"""
Import libraries
"""
import requests
import json


def weather_status(city_name, unit = 'metric'):

    """
    Create API request call.
    """
    api_key = "813729884e6a2563a55305dc7ed7b63f"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + unit
    response = requests.get(complete_url)

    """
    Check for Status Code and print responses.
    """
    if response.status_code == 200:
        print('Success!')  
    elif response.status_code == 404:
        print('Resource not found.')
    elif response.status_code == 500:
        print('Server error.')
    elif response.status_code == 401:
        print('Unauthorized. Authentication required.')
    elif response.status_code == 403:
        print('Forbidden. Access denied.')
    else:
        print(f'Error: {response.status_code}')


    """
    Extracting required attributes from the API response
    and printing them.
    """

    '''Key Attributes Extraction'''
    data = response.json()
    city_name = data['name']
    temp = data['main']['temp']
    weather_des = data['weather'][0]['main'] + ', ' + data['weather'][0]['description']
    hum_level = data['main']['humidity']
    wind_speed = data['wind']['speed']

    '''Key Attributes Printing'''
    print(f'City Name: {city_name}')
    print(f'Temperature: {temp}celcius')
    print(f'Weather Description : {weather_des}')
    print(f'Humidity level: {hum_level}g/kg')
    print(f'Wind Speed: {wind_speed}m/s')

def weather_forecast(city_name, unit = 'metric'):

    """
    Create API request call.
    """
    api_key = "813729884e6a2563a55305dc7ed7b63f"
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + unit
    response = requests.get(complete_url)

    """
    Error Handling
        1) Check for Status Code and print responses.
        2) Check for user input or network availability errors
    """
    if response.status_code == 200:
        print('Success!')  
        # print(response.json())
    elif response.status_code == 404:
        print('Resource not found.')
    elif response.status_code == 500:
        print('Server error.')
    elif response.status_code == 401:
        print('Unauthorized. Authentication required.')
    elif response.status_code == 403:
        print('Forbidden. Access denied.')
    else:
        print(f'Error: {response.status_code}')

    


    """
    Extracting required attributes from the API response
    and printing them.
    Extracting the last day of forecast data for preview
    """

    data = response.json()
    city_name = data['city']['name']
    date = data['list'][-1]['dt_txt']
    temp = data['list'][-1]['main']['temp']
    # temp = round(temp-273.15,1)
    weather_des = data['list'][-1]['weather'][0]['main'] + ', ' + data['list'][-1]['weather'][0]['description']
    hum_level = data['list'][-1]['main']['humidity']
    wind_speed = data['list'][-1]['wind']['speed']

    print(f'City Name: {city_name}')
    print(f'Date: {date}')
    print(f'Temperature: {temp}celcius')
    print(f'Weather Description : {weather_des}')
    print(f'Humidity level: {hum_level}g/kg')
    print(f'Wind Speed: {wind_speed}m/s')

def mul_cities_weather_status(cities):
    
    #Error handling to ensure cities entry is a list
    if not isinstance(cities, list):
        raise TypeError("Cities parameter must be a list.")

    #Loops through entries in the cities and runs a weather status 
    # for the expected attributes per city
    for city in cities:
        print(weather_status(city_name=city))

def mul_cities_weather_forcast(cities):

    #Error handling to ensure cities entry is a list
    if not isinstance(cities, list):
        raise TypeError("Cities parameter must be a list.")
    
    #Loops through entries in the cities and runs a weather forecast 
    # for the expected attributes per city
    for city in cities:
        print(weather_forecast(city_name=city))


print('Single City API Calls\n')
print(weather_status(city_name='Osogbo'))
print(weather_forecast(city_name='Lagos'))
print('\n\n')

print('Multiple Cities API Calls\n')
print(mul_cities_weather_status(['Kano','Abuja']))
print('\n\n')
print(mul_cities_weather_status(['Kano','Abuja']))

# #Testing Error Handling for multiple cities
# print('Multiple Cities API Calls\n')
# print(mul_cities_weather_status('Ibadan'))
# print('\n\n')
# print(mul_cities_weather_status('Ibadan'))

#Testing Error Handling for single cities
print('Single City API Calls\n')
print(weather_status(city_name=['Osogbo', 'Ado-Ekiti']))
print(weather_forecast(city_name='Lagos'))
print('\n\n')