import json
import psycopg2
from psycopg2.extras import RealDictCursor
from constants import required_env_vars

def connect_database():
    try:
        conn = psycopg2.connect(
        host=required_env_vars['db_url'],
        database=required_env_vars['db_name'],
        user=required_env_vars['db_username'],
        password=required_env_vars['db_password']
        )
        return conn
        
    except psycopg2.Error as e:
        print("Database Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({"message": "Internal Server Error"})
        }