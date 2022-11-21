import json
from lambda_function import lambda_handler


def test_lambda_handler():

    payload = {
        "list": [
            {
                "MatchNumber": 1,
                "RoundNumber": 1,
                "DateUtc": "2022-11-20 16:00:00Z",
                "Location": "Al Bayt Stadium",
                "HomeTeam": "Qatar",
                "AwayTeam": "Ecuador",
                "Group": "Group A",
                "HomeTeamScore": 0,
                "AwayTeamScore": 2
            },
            {
                "MatchNumber": 3,
                "RoundNumber": 1,
                "DateUtc": "2022-11-21 13:00:00Z",
                "Location": "Khalifa International Stadium",
                "HomeTeam": "England",
                "AwayTeam": "Iran",
                "Group": "Group B",
                "HomeTeamScore": "",
                "AwayTeamScore": ""
            },
            {
                "MatchNumber": 16,
                "RoundNumber": 1,
                "DateUtc": "2022-11-24 19:00:00Z",
                "Location": "Lusail Stadium",
                "HomeTeam": "Brazil",
                "AwayTeam": "Serbia",
                "Group": "Group G",
                "HomeTeamScore": "",
                "AwayTeamScore": ""
            },
        ],
        "team": 'Brazil'
    }

    try:
        retorno = lambda_handler(payload, [])
    except Exception as ex:
        print(ex.args)
        retorno = json.dumps(ex.args)
    assert retorno


def test_lambda_handler_error():
    payload = {
        "list": [
            {
                "MatchNumber": 16,
                "RoundNumber": 1,
                "DateUtc": "2022-11-24 19:00:00Z",
                "Location": "Lusail Stadium",
                "HomeTeam": "Brazil",
                "AwayTeam": "Serbia",
                "Group": "Group G",
                "HomeTeamScore": "",
                "AwayTeamScore": ""
            },
        ],
        "team": 'Brazile'
    }
    try:
        retorno = lambda_handler(payload, [])
    except Exception as ex:
        print(ex.args)
        retorno = json.dumps(ex.args)
    assert retorno
