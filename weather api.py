import requests

lat =22.8056
lon =86.2031
api_key = "a619da88b81121a6f84b1edf24e55c79"

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()
print("City:", data['name'])
print('weather is ', data['weather'][0]['description'])
print('temperature is ', data['main']['temp'])
print('feels like temperature is ', data['main']['feels_like'])
print('humidity is ', data['main']['humidity'])
