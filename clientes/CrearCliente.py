import boto3

def lambda_handler(event, context):
    # Entrada (json)
    cliente = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('clientes')
    response = table.put_item(Item=curso)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
