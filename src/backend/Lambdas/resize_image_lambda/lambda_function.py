import json
import boto3
from PIL import Image
from urllib.parse import urlparse
from io import BytesIO

def lambda_handler(list_of_event, context):
    for record in list_of_event['Records']:
        
        event = json.loads(record['body'])
        
        o = urlparse(event['s3_url'], allow_fragments=False)
        bucket = o.netloc
        key = o.path[1:]
        
        s3 = boto3.resource('s3', region_name='us-east-1')
        bucket = s3.Bucket(bucket)
        img = bucket.Object(key).get().get('Body').read()
        im = Image.open(BytesIO(img))
        
        width = int(event['width'])
        height = int(event['height'])
        dim = (width, height)
          
        # resize image
        im1 = im.resize(dim)
        
        in_mem_file = BytesIO()
        im1.save(in_mem_file, format='JPEG')
        in_mem_file.seek(0)
        
        s3 = boto3.client('s3')
        s3.put_object(
            Body = in_mem_file, # This is what i am trying to upload
            Bucket = o.netloc,
            Key = event['save_path']
        )
    
    return "yay"