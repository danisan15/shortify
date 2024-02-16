import hashlib

def generate_code(url):
    # Generate a hash of the URL
    hash_object = hashlib.md5(url.encode())
    hash_code = hash_object.hexdigest()

    # Take the first 8 characters of the hash code
    short_code = hash_code[:8]

    return short_code
