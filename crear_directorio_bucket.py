import boto3
import json

def lambda_handler(event, context):
    # Verificar si event["body"] es una cadena JSON
    if isinstance(event["body"], str):
        body = json.loads(event["body"])
    else:
        body = event["body"]

    # Obtener el nombre del bucket y el nombre del "directorio"
    nombre_bucket = body["name"]
    nombre_directorio = body["directory_name"]

    try:
        s3 = boto3.client("s3")
        
        # Crear un objeto en S3 que simula un directorio
        s3.put_object(Bucket=nombre_bucket, Key=f"{nombre_directorio}/")
        
        # Retornar respuesta exitosa
        return {
            "statusCode": 201,
            "message": f"Directorio '{nombre_directorio}' creado en el bucket '{nombre_bucket}'"
        }

    except Exception as e:
        # Captura y muestra el mensaje de error detallado
        return {
            "statusCode": 400,
            "message": f"No se pudo crear el directorio: {str(e)}"
        }












