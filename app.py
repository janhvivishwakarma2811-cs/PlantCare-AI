from flask import Flask, render_template, request, send_from_directory
from src.disease_info import DISEASE_INFO
from werkzeug.utils import secure_filename
import os

from src.predict import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No image uploaded."

    file = request.files["image"]

    if file.filename == "":
        return "Please select an image."

    filename = secure_filename(file.filename)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)

    disease, confidence = predict_image(filepath)
    if confidence >= 90:
        confidence_level = "🟢 High Confidence"
    elif confidence >= 70:
        confidence_level = "🟡 Medium Confidence"
    else:
        confidence_level = "🔴 Low Confidence"
    info = DISEASE_INFO.get(
    disease,
    {
        "name": disease,
        "description": "Information not available.",
        "treatment": [],
        "prevention": []
    }
)

    return render_template(
    "result.html",
    disease=info["name"],
    confidence=round(confidence, 2),
    confidence_level=confidence_level,
    image_file=filename,
    description=info["description"],
    treatment=info["treatment"],
    prevention=info["prevention"],
)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
if __name__ == "__main__":
    app.run(debug=True)