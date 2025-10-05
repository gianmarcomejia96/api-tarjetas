import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tarjeta_id = event['body']['tarjeta_id']
    datos = event['body']['datos']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tarjetas')
    response = table.update_item(
        Key={
            'cliente_id': tarjeta_id
        },
        UpdateExpression="set datos=:datos_a_actualizar",
        ExpressionAttributeValues={
            ':datos_a_actualizar': datos
        },
        ReturnValues="UPDATED_NEW"
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
