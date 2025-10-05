import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tarjeta = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tarjetas')
    response = table.put_item(Item=tarjeta)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
