API_KEYS = {
    "bg-be24e8bd47c13f0f5568a2cc6810fd3d": {
        "label": "primary",
        "created_at": "2026-04-17"
    }
}

def validate_api_key(api_key):
    return api_key in API_KEYS
