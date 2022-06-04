import json
from decimal import Decimal

import boto3
import uuid
import base64

def lambda_handler(event, context):
    bucket_name = 'telematics-images-raw'
    dynamodb_table_name = 'telematics-images-metadata'
    
    s3 = boto3.resource('s3', region_name='us-east-1')
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    photo_id = str(uuid.uuid4())
    
    # The request comes as a dictionary
    payload = json.loads(event['body'], parse_float=Decimal)
    
    # Put image out in s3
    image = base64.b64decode(payload['image'])
    image_path = f"images/{photo_id}.jpeg"
    object = s3.Object(bucket_name, image_path)
    object.put(Body = image, ContentType = 'image/jpeg')
    
    # Put metadata in dynamodb
    table = dynamodb.Table(dynamodb_table_name)
    table.update_item(
        Key = {'trip_id': payload['trip_id']},
        UpdateExpression = ' SET photos = list_append(if_not_exists(photos, :empty), :photos)',    
        ExpressionAttributeValues  = {
            ':empty': [],
            ':photos': [{
                'timestamp': payload['timestamp'],
                'image_path': f"s3://{bucket_name}/{image_path}",
                'lat': payload['lat'],
                'long': payload['long'],
                'accuracy': payload['accuracy'],
                'speed': payload['speed']
                }]
            }
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('File Processed')
    }
