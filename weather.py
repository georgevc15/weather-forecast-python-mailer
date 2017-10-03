import requests

def get_weather_forecast():
    # Connecting to the weather api
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid=ace81c554edf6297e213326bfe5ed2ac'
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    #print(weather_json)

    #Parsing JSON
    description = weather_json['weather'][0]['description']
    #print(description)
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    #print(temp_min)
    #print(temp_max)
    
    # Creating our forecast string
    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast
