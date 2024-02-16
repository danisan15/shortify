import os

required_env_vars = {
    'db_url': os.environ.get('db_url'),
    'db_username': os.environ.get('db_username'),
    'db_password': os.environ.get('db_password'),
    'db_name': os.environ.get('db_name'),
    'domain_url': os.environ.get('domain_url')
}

