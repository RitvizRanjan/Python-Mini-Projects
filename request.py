  
import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=56db57c328982a961e211c325734a760&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
print(json_data)