import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    tarjeta_id = event['body']['tarjeta_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tarjetas')
    response = table.query(
        KeyConditionExpression=Key('tarjeta_id').eq(tarjeta_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }
