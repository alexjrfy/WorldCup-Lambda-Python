import requests
from lambda_function import lambda_handler

strUrl = 'https://fixturedownload.com/feed/json/fifa-world-cup-2022'
listWorldCup = requests.get(strUrl).json()
team = 'Brazil'

payload = {
    "list": listWorldCup,
    "team": team
}

print(lambda_handler(payload, ''))
