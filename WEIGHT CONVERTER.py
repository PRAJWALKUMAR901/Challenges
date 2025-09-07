import requests
import webbrowser

API_KEY = "cc64cee3400753faf34c43a89ad622f6"

city = input("Enter City: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]

    print(f"Temperature: {temp}")
    print(f"Weather: {weather}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Wind speed: {wind}")

    html_content = f"""
     <html>
     <head><title>Weather Report</title></head>
     <body>
         <h1>Weather of {city}</h1>
         <p><b>Temperature is </b> {temp} °C</p>
         <p><b>Condition is </b> {weather}</p>
         <p><b>Humidity is </b> {humidity}%</p>
         <p><b>Pressure is </b> {pressure} hPa</p>
         <p><b>Wind Speed is </b> {wind} m/s</p>
     </body>
     </html>
     """
    fp="weather.html"
    with open(fp, "w") as file:
        file.write(html_content)


    webbrowser.open(fp)

else:
    print(" City not found! your city name is invalid please check the city name and try again.")