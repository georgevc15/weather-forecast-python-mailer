import requests
import smtplib

def get_emails():
    emails = {}


    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:
            (email,name) = line.split(',')
            emails[email] = name.strip()
        
    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')

        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule

def get_weather_forecast():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid=ace81c554edf6297e213326bfe5ed2ac'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    print(weather_json)

    description = weather_json['weather'][0]['description']
    print(description)
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    print(temp_min)
    print(temp_max)

    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast

def send_emails(emails, schedule, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = input("What's your password?")
    from_email = 'george.codattudoran@gmail.com'
    server.login(from_email, password)

    # Send email to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the Circus!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += 'Hope to seeyou there!'
        server.sendmail(from_email, to_email, message)


    server.quit()

                          

def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    forecast = get_weather_forecast()
    print(forecast)

    send_emails(emails, schedule, forecast)
                                                       
main()

                                                
