import json
from psycopg2.extras import RealDictCursor
from DB_connection import connect_database

def lambda_handler(event, context):
    try:    
        conn = connect_database()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute(f"SELECT shortened_url FROM urls")
        urls = cur.fetchall() 

        shortened_url_ids = [{'shortenedUrl': url['shortened_url'].split('/')[-1]} for url in urls]

        return {
            'statusCode': 200,
            'body': json.dumps(shortened_url_ids)
        }
    except:
        return {
            'statusCode': 500,
            'body': json.dumps("There was an error")
        }
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
