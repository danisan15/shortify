import os
import json
import psycopg2
import datetime
import urllib.request
from constants import required_env_vars
from url_validator import validate_url
from code_generator import generate_code
from psycopg2.extras import RealDictCursor

def lambda_handler(event, context):
    print(required_env_vars)
    
    for env_var, var_description in required_env_vars.items():
        if os.environ.get(env_var) is None:
            raise ValueError(f"Missing environment variable: {var_description}")
    
    print("Environment variables imported successfully")
    
    # Establish database connection
    try:
        conn = psycopg2.connect(
        host=required_env_vars['db_url'],
        database=required_env_vars['db_name'],
        user=required_env_vars['db_username'],
        password=required_env_vars['db_password']
    )

        cur = conn.cursor(cursor_factory=RealDictCursor)
        body = json.loads(event["body"])
        print(body)
        url = body["url"]
        if 'username' in body:
            username = body["username"]

        code = generate_code(url)
        base_url = required_env_vars['domain_url']
        shortened_url = base_url + code

        cur.execute('SELECT url_code FROM urls WHERE url_code = %s', (code,))
        existing_code = cur.fetchone()

        if existing_code:
            return {
                'statusCode': 200,
                'body': json.dumps({"shortenedUrl": shortened_url})
            }

        if not validate_url(url):
            return {
                'statusCode': 400,
                'body': json.dumps({"message": "Invalid URL"})
            }

        current_timestamp = datetime.datetime.now()

        if 'username' in locals():
            cur.execute('INSERT INTO urls (original_url, url_code, created_on, username) VALUES (%s, %s, %s, %s)',
                        (url, code, current_timestamp, username))
            print("Successfully inserted with username")
        else:
            cur.execute('INSERT INTO urls (original_url, url_code, created_on) VALUES (%s, %s, %s)',
                        (url, code, current_timestamp))
            print("Successfully inserted without username")

        conn.commit()

        return {
            'statusCode': 200,
            'body': json.dumps({"shortenedUrl": shortened_url})
        }

    except psycopg2.Error as e:
        print("Database Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({"message": "Internal Server Error"})
        }
    
    except (ValueError, KeyError) as e:
        print("JSON Parsing Error:", str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({"message": "Invalid JSON"})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({"message": "Internal Server Error"})
        }
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()