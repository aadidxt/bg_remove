from flask import Blueprint, request, send_file, jsonify
import io
from app.services.bg_remove import remove_background
from app.utils.limiter import check_limit
from app.models.user import create_user, get_today_usage, get_users_register
from app.auth import validate_api_key

api = Blueprint("api", __name__)


def require_api_key():
    api_key = request.headers.get("x-api-key")
    if not api_key or not validate_api_key(api_key):
        return jsonify({"error": "Invalid API Key"}), 401
    return None


@api.route("/v1/session", methods=["POST"])
def create_session():
    auth_error = require_api_key()
    if auth_error:
        return auth_error

    uid = create_user()
    usage = get_today_usage(uid)
    return jsonify({"uid": uid, "usage": usage}), 201


@api.route("/v1/usage", methods=["GET"])
def usage():
    auth_error = require_api_key()
    if auth_error:
        return auth_error

    uid = request.headers.get("x-user-id")
    if not uid:
        return jsonify({"error": "Missing user id"}), 400
    return jsonify(get_today_usage(uid)), 200


@api.route("/v1/users", methods=["GET"])
def users_register():
    auth_error = require_api_key()
    if auth_error:
        return auth_error

    return jsonify({"users": get_users_register()}), 200


@api.route("/v1/remove-bg", methods=["POST"])
def remove_bg():
    limit_check, usage = check_limit()
    if limit_check:
        return limit_check

    if "image" not in request.files:
        return jsonify({"error": "No file"}), 400

    file = request.files["image"]
    input_bytes = file.read()

    try:
        output = remove_background(input_bytes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    response = send_file(io.BytesIO(output), mimetype="image/png")
    response.headers["X-Usage-Used"] = str(usage["used"])
    response.headers["X-Usage-Limit"] = str(usage["limit"])
    response.headers["X-Usage-Date"] = usage["date"]
    response.headers["X-User-Id"] = usage["uid"]
    return response
