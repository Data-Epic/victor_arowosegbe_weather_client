from prefect import flow, task

@task(name='Weather API Task')
def weather_client(city_name: str):
    import requests
    import json
    from dotenv import load_dotenv
    import os

    load_dotenv()
    Key = os.getenv('APIKey')
    unit = 'metric'
    try:
       base_url = "http://api.openweathermap.org/data/2.5/weather?"
       complete_url = base_url + "appid=" + Key + "&q=" + city_name + "&units=" + unit
       response = requests.get(complete_url) 

       if response.status_code == 200:
            print('Success!')  
            data = response.json()
            return data
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

    except requests.exceptions.ConnectionError:
        print("Connection error, please check internet connection")

    except requests.exceptions.Timeout:
        print("Requests timed out")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

@task(name = 'Gspread Automation Task')
def gspread_automation_weather_data(data: dict):
    import gspread
    import sys
    import prefect
    from google.oauth2.service_account import Credentials
    import google

    try:

        scopes = ['https://www.googleapis.com/auth/drive.file']
        json_file = "C:/Users/APIN PC/OneDrive/Documents/DS/Git Repos/Data Epic/victor_arowosegbe/prefect-demo/environment/credentials.json"
        credentials = Credentials.from_service_account_file(json_file, scopes=scopes)
        gc = gspread.authorize(credentials)
        sh = gc.open('Gspread_Automation_Data')
        ws = sh.worksheet('Sheet1')
        # # sh = gc.open('Weather_Data').sheet1
        # sh = gc.open('Automation Task').sheet1

        '''Key Attributes Extraction'''
        city_name = data['name'] #Extracts the name of the city from the dictionary
        temp = data['main']['temp'] #Extracts the average temperature of the city from the dictionary
        weather_des = data['weather'][0]['main'] + ', ' + data['weather'][0]['description'] #Extracts two weather info and joins them
        hum_level = data['main']['humidity'] #Extracts the humidity of the city from the dictionary
        wind_speed = data['wind']['speed'] #Extracts the wind speed of the city from the dictionary

        body = [city_name, temp, weather_des, hum_level, wind_speed]

        ws.append_row(body)

    except gspread.exceptions.APIError:
        print("Failed to connect to Google Sheets API")
        sys.exit(1)
    
    except prefect.exceptions.ParameterBindError:
        print(f"Error binding parameters for function 'gspread_automation_weather_data': too many positional arguments.")
        sys.exit(1)

    except google.auth.exceptions.RefreshError:
        print(f"invalid_grant: Token has been expired or revoked.")
        sys.exit(1)

    except FileNotFoundError:
        print("Json credential file not found")
        sys.exit(1)

    else: 
        print("Orchestration Task Successful!!")

    finally:
        print('Task Complete!!')

@flow(name= 'Orchestration Task', log_prints=True)
def ochestration_prefect(city_name:str):
    """
    Performs an ochestration flow for the weather_client API task and the Google sheet API task.__annotations__

    Args:
        city_name (str): name of the city to check for its weather status and input in the Weather Data 
    """
    data = weather_client(city_name)
    gspread_automation_weather_data(data)

if __name__ == '__main__':
    """
    Main program entry point. It prompts the user for city name. Then it 
    calls the 'ochestration_prefect' function to fetch and run the flow.
    """
    user_input = input('Kindly input a specific city: ').strip().lower()
    ochestration_prefect(user_input)

'''
Steps to starting the server and running flows
1) create a terminal for the prefect package. (Ctrl+Shift+`)
2) type 'prefect server start' and run in the terminal.
3) now run your python script with the preferred module(s) in the prefect package called.
'''


