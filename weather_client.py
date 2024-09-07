"""
Import libraries
"""
import requests
import json


def weather_status(city_name, unit = 'metric'):
    """
    This function creates an API call to the Openweatherapp API and generates weather
    status for a verified city inputed. 


    Args:
        city_name (str): The name of a city in any of the countries updated on Openweatherapp API.
        unit (str, optional): _description_. Defaults to 'metric'.

    Exception Handling:
    It reviews the status codes of the request and correlates it to a suitable response.
    Below are the main status codes and meaning.
        200 : Success
        404 : Resource not found.Kindly check the spelling of the city name.
        505 : Server error.Kindly check the internet connection.
        401 : Unauthorized. Authentication required. Kindly input your API key or check its authenticity.
        403 : Forbidden. Access denied. Wrong API call. Kindly obtained required access.

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
        # print(response.json())
    elif response.status_code == 404:
        print('Resource not found.\
            Kindly check the spelling of the city name')
    elif response.status_code == 500:
        print('Server error.\
            Kindly check the internet connection.')
    elif response.status_code == 401:
        print('Unauthorized. Authentication required.\
            Kindly input your API key or check its authenticity.')
    elif response.status_code == 403:
        print('Forbidden. Access denied.\
            Wrong API call. Kindly obtained required access')
    else:
        print(f'Error: {response.status_code}')

    """
    Extracting required attributes from the API response
    and printing them.
    """

    '''Key Attributes Extraction'''
    data = response.json() #Converts the json file to python dictionary
    city_name = data['name'] #Extracts the name of the city from the dictionary
    temp = data['main']['temp'] #Extracts the average temperature of the city from the dictionary
    weather_des = data['weather'][0]['main'] + ', ' + data['weather'][0]['description'] #Extracts two weather info and joins them
    hum_level = data['main']['humidity'] #Extracts the humidity of the city from the dictionary
    wind_speed = data['wind']['speed'] #Extracts the wind speed of the city from the dictionary

    '''Key Attributes Printing'''
    print(f'City Name: {city_name}')
    print(f'Temperature: {temp}celcius')
    print(f'Weather Description : {weather_des}')
    print(f'Humidity level: {hum_level}%')
    print(f'Wind Speed: {wind_speed}m/s')

def weather_forecast(city_name, unit = 'metric'):

    """
    This function creates an API call to the Openweatherapp API and generates a 5 day weather
    forecast for a verified city inputed. 

    Args:
        city_name (str): The name of a city in any of the countries updated on Openweatherapp API.
        unit (str, optional): The unit attribute converts temperature from kelvin to degree celcius. Defaults to 'metric'.

    Exception Handling:
    It reviews the status codes of the request and correlates it to a suitable response.
    Below are the main status codes and meaning.
        200 : Success
        404 : Resource not found.Kindly check the spelling of the city name.
        505 : Server error.Kindly check the internet connection.
        401 : Unauthorized. Authentication required. Kindly input your API key or check its authenticity.
        403 : Forbidden. Access denied. Wrong API call. Kindly obtained required access.

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
        print('Resource not found.\
            Kindly check the spelling of the city name')
    elif response.status_code == 500:
        print('Server error.\
            Kindly check the internet connection.')
    elif response.status_code == 401:
        print('Unauthorized. Authentication required.\
            Kindly input your API key or check its authenticity.')
    elif response.status_code == 403:
        print('Forbidden. Access denied.\
            Wrong API call. Kindly obtained required access')
    else:
        print(f'Error: {response.status_code}')
    
    """
    Extracting required attributes from the API response
    and printing them.
    Extracting the last day of forecast data for preview
    """

    data = response.json() #Converts the json file to python dictionary of the forecast data.
    city_name = data['city']['name'] #Extracts the name of city from the dictionary
    date = data['list'][-1]['dt_txt'] #Extracts the forecast date (5th day forcast)
    temp = data['list'][-1]['main']['temp'] #Extracts the average temperature of the city in celcius
    weather_des = data['list'][-1]['weather'][0]['main'] + ', ' + data['list'][-1]['weather'][0]['description']#Extracts two weather info and joins them
    hum_level = data['list'][-1]['main']['humidity'] #Extracts the humidity in the city
    wind_speed = data['list'][-1]['wind']['speed'] #Extracts the wind speed in the city.

    print(f'City Name: {city_name}')
    print(f'Date: {date}')
    print(f'Temperature: {temp}celcius')
    print(f'Weather Description : {weather_des}')
    print(f'Humidity level: {hum_level}%')
    print(f'Wind Speed: {wind_speed}m/s')

def mul_cities_weather_status(cities):
    """
    This function enables the user to input multiple cities and get the weather status for all of them.
    It's only input is a list.

    Args:
        cities (list): List of cities to obtain weather status for

    Raises:
        TypeError: Raises a TypeError for any other input apart from a list
    """    
    
    #Error handling to ensure cities entry is a list
    if not isinstance(cities, list):
        raise TypeError("Cities parameter must be a list.")

    #Loops through entries in the cities and runs a weather status 
    # for the expected attributes per city
    for city in cities:
        print(weather_status(city_name=city))

def mul_cities_weather_forecast(cities):
    """
    This function enables the user to input multiple cities and get the weather forecast for all of them.
    It's only input is a list.

    Args:
        cities (list): List of cities to obtain weather forecast for.

    Raises:
        TypeError: Raises a TypeError for any other input apart from a list
    """   

    #Error handling to ensure cities entry is a list
    if not isinstance(cities, list):
        raise TypeError("Cities parameter must be a list.")
    
    #Loops through entries in the cities and runs a weather forecast 
    # for the expected attributes per city
    for city in cities:
        print(weather_forecast(city_name=city))


