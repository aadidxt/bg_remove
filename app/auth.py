import uuid

API_KEYS = {
    "test-key-123": {"limit": 100, "used": 0}
}

def generate_api_key():
    return str(uuid.uuid4())

def validate_api_key(key):
    return key in API_KEYS