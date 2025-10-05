import boto3

def lambda_handler(event, context):
    # Entrada (json)
    operacion_id = event['body']['operacion_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('operaciones')
    response = table.delete_item(
        Key={
            'operacion_id': operacion_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
