import requests
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    city_encoded = urllib.parse.quote(city)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid=4f74e4a0ce8b67f829e7ef0e4c26ebb1&lang=pt_br&units=metric"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data["weather"][0]["description"]
        print(f"Clima em {city}: {description}, {temp}ºC")
    else:
        print(f"Erro {response.status_code} Cidade não encontrada ou erro na API")

if __name__ == "__main__":
    cidade = input("Digite o nome da cidade: ")
    get_weather(cidade)