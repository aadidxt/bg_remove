from flask import Blueprint, request, send_file, jsonify
import io
from app.services.bg_remove import remove_background
from app.utils.limiter import check_limit

api = Blueprint("api", __name__)

@api.route("/v1/remove-bg", methods=["POST"])
def remove_bg():
    limit_check = check_limit()
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

    return send_file(io.BytesIO(output), mimetype="image/png")