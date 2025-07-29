import boto3
import csv
import psycopg2
import os

def lambda_handler(event, context):

    # 1. Récupérer le nom du bucket et du fichier depuis l'event S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    key    = event['Records'][0]['s3']['object']['key']

    print(f" Processing file: s3://{bucket}/{key}")

    # 2. Lire le fichier CSV depuis S3
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    lines = obj['Body'].read().decode('utf-8').splitlines()
    reader = csv.reader(lines)
    headers = next(reader)  # skip header

    # 3. Connexion à PostgreSQL
    conn = psycopg2.connect(
        host=os.environ['PG_HOST'],
        dbname=os.environ['PG_DB'],
        user=os.environ['PG_USER'],
        password=os.environ['PG_PASS'],
        port=os.environ.get('PG_PORT', 5432)
    )
    cur = conn.cursor()

    # 4. Insérer les lignes dans une table 
    for row in reader:
        cur.execute(
            "INSERT INTO data_table (col1, col2, col3) VALUES (%s, %s, %s)",
            row
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted successfully.")
