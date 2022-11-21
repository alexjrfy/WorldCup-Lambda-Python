from src.utils.customException import CustomException
from http import HTTPStatus
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    OutputObj = []
    try:
        
        teamMatches = []
        for match in event['list']:
            if match['HomeTeam'] ==event['team'] or match['AwayTeam']==event['team']:
                teamMatches.append(match)
        
        if len(teamMatches)>0:
            OutputObj = {
                'statusCode': HTTPStatus.OK.value,
                'headers':{
                    "Content-Type": "application/json"
                },
                'body': teamMatches
            }
            
        else:
            raise CustomException({'errorMessage':'Invalid Team'})
    except Exception as ex:
        OutputObj = {
                'statusCode': HTTPStatus.BAD_REQUEST.value,
                'headers':{
                    "Content-Type": "application/json"
                },
                'body': ex.args
            }
        
    return json.dumps(OutputObj)
    