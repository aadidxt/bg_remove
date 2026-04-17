from flask import request, jsonify
from app.models.user import consume_usage
from app.auth import validate_api_key

def check_limit():
    uid = request.headers.get("x-user-id")
    api_key = request.headers.get("x-api-key")

    if not api_key or not validate_api_key(api_key):
        return (jsonify({"error": "Invalid API Key"}), 401), None

    if not uid:
        return (jsonify({"error": "Missing user id"}), 400), None

    usage = consume_usage(uid)

    if not usage["allowed"]:
        return (jsonify({
            "error": "Daily usage limit exceeded",
            "uid": usage["uid"],
            "date": usage["date"],
            "used": usage["used"],
            "limit": usage["limit"],
        }), 429), None

    return None, usage
