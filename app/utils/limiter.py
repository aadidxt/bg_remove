from flask import request, jsonify
from app.auth import API_KEYS

def check_limit():
    api_key = request.headers.get("x-api-key")

    if api_key not in API_KEYS:
        return jsonify({"error": "Invalid API Key"}), 401

    user = API_KEYS[api_key]

    if user["used"] >= user["limit"]:
        return jsonify({"error": "Usage limit exceeded"}), 429

    user["used"] += 1
    return None