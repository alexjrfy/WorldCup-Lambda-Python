from src.models.enumStatusCode import StatusCode
import logging
import json

def lambda_handler(event, context):
    
    try:
        OutputObj = []
        teamMatches = []
        for match in event['list']:
            if match['HomeTeam'] ==event['team'] or match['AwayTeam']==event['team']:
                teamMatches.append(match)
        
        if len(teamMatches)>0:
            jsonOutout = json.dumps(teamMatches)
            OutputObj = {
                'statusCode': StatusCode.BAD_REQUEST.value,
                'headers':{
                    "Content-Type": "application/json"
                },
                'body': jsonOutout
            }

            return OutputObj
        else:
            raise Exception('Invalid Team')