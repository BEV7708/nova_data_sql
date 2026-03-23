import psycopg2
import os
import sys
import random
from dotenv import load_dotenv

load_dotenv('D:/data_sql/nova_data_sql/.env')

required_vars=['POSTGRES_USER', 'POSTGRES_PASSWORD', 'POSTGRES_HOST', 'POSTGRES_PORT', 'POSTGRES_DB']
missing_vars=[var for var in required_vars if not os.getenv(var)]
if missing_vars:
    print(f"Отсутствуют переменные: {missing_vars}")

user=os.getenv('POSTGRES_USER')
password=os.getenv('POSTGRES_PASSWORD')
db=os.getenv('POSTGRES_DB')
host=os.getenv('POSTGRES_HOST')
port=os.getenv('POSTGRES_PORT')

conn_params = {
    'dbname': 'demo'
    'user': f'{user}'
}