import boto3
import json

def lambda_handler(event, context):
    # Verificar si event["body"] es una cadena JSON
    if isinstance(event["body"], str):
        body = json.loads(event["body"])
    else:
        body = event["body"]

    # Obtener el nombre del bucket
    nombre_bucket = body["name"]

    try:
        s3 = boto3.client("s3")
        
        s3.create_bucket(
            Bucket=nombre_bucket,
            ObjectOwnership="BucketOwnerPreferred"
        )
        
        s3.put_public_access_block(
            Bucket=nombre_bucket,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )
        
        s3.put_bucket_acl(ACL='public-read-write', Bucket=nombre_bucket)
        
        return {
            "statusCode": 201,
            "bucket": nombre_bucket,
        }

    except Exception as e:
        # Captura y muestra el mensaje de error detallado
        return {
            "statusCode": 400,
            "message": f"No se pudo crear el bucket: {str(e)}"
        }
