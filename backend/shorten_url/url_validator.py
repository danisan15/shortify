import re

def validate_url(url):
    pattern = r"^(http|https)://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, url))