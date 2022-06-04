import json 
from decimal import Decimal
import boto3 
import asyncio

sagemaker_client = boto3.client('runtime.sagemaker')
rekog_client = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Reading in model configs
f = open('model_labels.json')
model_labels = json.load(f)

# Reading in rekognition target labels
f = open('rekog_label_targets.json')
rekog_label_targets = json.load(f)

async def run_sagemaker_model(payload, endpoint):
    """Runs async due to the long run time of models"""
    
    response = sagemaker_client.invoke_endpoint(
        EndpointName = endpoint,
        Body = payload,
        ContentType = "image/jpeg"
        )
        
    labels = model_labels[endpoint]
    probs = json.loads(response['Body'].read())
    predictions = dict(zip(labels, probs))
    
    return {
        'model_name': endpoint,
        'predictions': predictions
    }
    
async def run_rekog_detect_labels(payload):
    """Runs the Rekognition Detect Labels Endpoint"""
    
    response = rekog_client.detect_labels(
        Image = {'Bytes': payload},
        MinConfidence = 51
        )
    
    # Filter to only the labels we care about
    detections = [x for x in response['Labels'] 
                    if x['Name'] in rekog_label_targets]
    
    return {
        'model_name': 'rekognition_detect_labels',
        'predictions': detections
    }

def lambda_handler(event, context):

    # Read One Image
    s3 = boto3.resource('s3', region_name='us-east-1')
    bucket = s3.Bucket(event['bucket'])
    object = bucket.Object(event['key'])
    img_data = object.get().get('Body').read()
    
    # Send image to models
    loop = asyncio.get_event_loop()
    tasks = [
        run_sagemaker_model(payload = img_data, endpoint = 'scene'),
        run_sagemaker_model(payload = img_data, endpoint = 'weather'),
        run_sagemaker_model(payload = img_data, endpoint = 'timeofday'),
        run_rekog_detect_labels(payload = img_data)
        ]
        
    done, _ = loop.run_until_complete(asyncio.wait(tasks))
    results = [x.result() for x in done]
    
    # Prep item for dynamodb
    payload = {
        'trip_id': event['trip_id'], 
        'image_path': event['image_path'],
        'lat': event['lat'],
        'long': event['long'],
        'accuracy': event['accuracy'],
        'speed': event['speed'],
        'timestamp': event['timestamp'],
        'model_result': results
    }
    item = json.loads(json.dumps(payload), parse_float=Decimal)
    
    # Put payload into dynamodb
    table = dynamodb.Table("telematics-images-model-results")
    table.put_item(Item = item)
        
    return {
        'statusCode': 200,
        'body': json.dumps('File Processed')
    }
