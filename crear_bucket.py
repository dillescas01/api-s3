import boto3
import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket_name']
        
        s3 = boto3.client('s3')
        s3.create_bucket(Bucket=bucket_name)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Bucket {bucket_name} creado exitosamente.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
