import json
from psycopg2.extras import RealDictCursor
from DB_connection import connect_database

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        id = body["id"]
        
        
        conn =  connect_database()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("SELECT original_url FROM urls WHERE url_code = %s", (id,))
        original_url = cur.fetchone()

        return {
            'statusCode': 200,
            'body': json.dumps({"original_url": original_url["original_url"]})
        }
        
    except:
        return {
            'statusCode': 500,
            'body': json.dumps("There was an error")
        }
