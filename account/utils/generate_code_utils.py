import secrets

def generate_code():
    return str(secrets.randbelow(900000) + 100000)