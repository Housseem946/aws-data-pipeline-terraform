import os
from etl_handler import lambda_handler

# Simuler un événement S3
event = {
    'Records': [{
        's3': {
            'bucket': {'name': 'mon-bucket-test'},
            'object': {'key': 'sample.csv'}
        }
    }]
}

# Injecter les variables d'environnement
os.environ['PG_HOST'] = 'localhost'
os.environ['PG_DB'] = 'mydb'
os.environ['PG_USER'] = 'postgres'
os.environ['PG_PASS'] = 'postgres'

lambda_handler(event, None)
