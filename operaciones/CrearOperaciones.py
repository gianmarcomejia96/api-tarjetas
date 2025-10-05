import boto3

def lambda_handler(event, context):
    # Entrada (json)
    operacion = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('operaciones')
    response = table.put_item(Item=operacion)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
