import base64
import boto3
import json

def upload_base_64_to_s3(s3_bucket_name, s3_file_name, base_64_str):
    s3 = boto3.resource('s3')
    s3.Object(s3_bucket_name, s3_file_name).put(Body=base64.b64decode(base_64_str))
    return (s3_bucket_name, s3_file_name)

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket_name']
        directory_name = body['directory_name']
        file_name = body['file_name']
        base64_content = body['file_content']
        
        s3_file_name = f"{directory_name}/{file_name}"
        upload_base_64_to_s3(bucket_name, s3_file_name, base64_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Archivo {file_name} subido exitosamente a {directory_name} en el bucket {bucket_name}.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
