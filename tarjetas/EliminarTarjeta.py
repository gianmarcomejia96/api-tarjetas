import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tarjeta_id = event['body']['tarjeta_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tarjetas')
    response = table.delete_item(
        Key={
            'tarjeta_id': tarjeta_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
