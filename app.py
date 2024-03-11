import requests
import boto3
from datetime import datetime

def download_and_store_pages(event, context):
    # Descargar las 5 primeras páginas
    for i in range(1, 6):
        url = f"https://casas.mitula.com.co/pagina-{i}"
        response = requests.get(url)
        
        # Almacenar en S3
        bucket_name = 'parcial-def'
        key = f'casas/contenido-pag-{i}-{datetime.now().strftime("%Y-%m-%d")}.html'
        
        s3 = boto3.client('s3')
        s3.put_object(
            Body=response.content,
            Bucket=bucket_name,
            Key=key
        )

def handler(event, context):
    # Punto de entrada para Zappa
    download_and_store_pages(event, context)
