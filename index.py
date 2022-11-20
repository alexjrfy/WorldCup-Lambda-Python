import requests
from lambda_function import lambda_handler

listWorldCup = requests.get('https://fixturedownload.com/feed/json/fifa-world-cup-2022').json()
team = 'Brazil'

payload = {
    "list": listWorldCup,
    "team": team
}

print(lambda_handler(payload,''))
