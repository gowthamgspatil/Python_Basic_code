import requests



city = input("Enter city: ")
api_key = "21ec3ffaa8cce0df46af039d8c3839aa"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url).json()
print(f"Temperature: {response['main']['temp']}°C")
print(f"Weather: {response['weather'][0]['description']}")
