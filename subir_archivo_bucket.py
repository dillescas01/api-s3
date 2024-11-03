import boto3
import json
import base64

def lambda_handler(event, context):
    # Verificar si event["body"] es una cadena JSON
    if isinstance(event["body"], str):
        body = json.loads(event["body"])
    else:
        body = event["body"]

    # Obtener el nombre del bucket, el directorio y el archivo
    nombre_bucket = body["name"]
    nombre_directorio = body["directory_name"]
    nombre_archivo = body["file_name"]
    contenido_base64 = body["file_content"]

    try:
        # Decodificar el contenido del archivo desde base64
        file_content = base64.b64decode(contenido_base64)

        s3 = boto3.client("s3")
        
        # Crear el nombre completo de la clave (directorio + nombre del archivo)
        key = f"{nombre_directorio}/{nombre_archivo}"
        
        # Subir el archivo al bucket en la ubicación especificada
        s3.put_object(Bucket=nombre_bucket, Key=key, Body=file_content)
        
        # Retornar respuesta exitosa
        return {
            "statusCode": 201,
            "message": f"Archivo '{nombre_archivo}' subido correctamente en '{nombre_directorio}' dentro del bucket '{nombre_bucket}'"
        }

    except Exception as e:
        # Captura y muestra el mensaje de error detallado
        return {
            "statusCode": 400,
            "message": f"No se pudo subir el archivo: {str(e)}"
        }
