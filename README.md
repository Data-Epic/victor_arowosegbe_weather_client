# **Weather Data to Google Sheets Orchestration Project**  

## **Overview**   
This project demonstrates how to orchestrate two tasks: fetching weather data using an API and storing results in a Google Sheet.  
The workflow is managed using Prefect, a powerful oprchestration tool. The orchestration project builds upon two ideas:  
1. Automating Google sheets with Gspread
2. Fetching weather data using Weather API client - OpenWeatherMap
The goal is to automate the prrocess of fetching weather data for a city and storing it in a Google Sheet using Prefect's workflow capabilities.

## **Project Structure**   
1. Task 1(Fetch weather data): This functioon defines a Prefect taskk that fetches weather data from a specified city using the OpenWeather API.
2. Taak 2(Store in google sheet): This functioon defines a Prefect task that writes the fetched weather data to a Google Sheet using Gspread library.
3. Flow (Weather to Sheets): This the mainn orchestration function that combines the two tasks into a Prefectt workflow.
4. Credential file:: This file conttains the Google API credentials for accessing the GooglE Sheet.

## **Requirements**   
1. Prefect
2. Gspread
3. Requests
4. oauth2client
5. OpenWeather API key - for the weather data
6. Google service account for google sheet access

## ** User Functionality**
The program allows a user to enter the name of city, fetches the data from the Weather API and updates the fetched weather data in the encoded google spread sheet. 

## **Look Ahead**
Looking ahead, the next version's goal is to allow users;
1. Input multiple cities and update weather data per cities to new rows.
2. Add a weather forecast functionality task which enable the user request for weather forecast of a city or cities.

## **Conclusion**   
This Orchestration Project combines weather data fetching and Google Sheets automation into a seamless workflow using Prefect. The project orchestrates the two tasks for easy automationn and data storage. 