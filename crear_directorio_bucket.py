import boto3
import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket_name']
        directory_name = body['directory_name']
        
        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Directorio {directory_name} creado en el bucket {bucket_name}.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
