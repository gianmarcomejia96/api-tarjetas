import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    operacion_id = event['body']['operacion_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('operaciones')
    response = table.query(
        KeyConditionExpression=Key('operacion_id').eq(operacion_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }
