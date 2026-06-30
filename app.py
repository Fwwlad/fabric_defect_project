from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

import os

from config import (
    UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH
)

from predict import process_image

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    if "image" not in request.files:
        return jsonify({"error": "Файл не найден"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "Файл не выбран"}), 400

    filename = secure_filename(file.filename)

    upload_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(upload_path)

    result = process_image(upload_path)

    return jsonify({
        "count": result["cup_count"],
        "time": result["processing_time"],
        "image": f"/static/results/{filename}"
    })


if __name__ == "__main__":
    app.run(debug=True)