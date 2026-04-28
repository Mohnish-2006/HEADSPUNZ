from flask import Flask, jsonify
from flask_cors import CORS

from camera import detect_faces
from stats import add_stat, get_stats, get_suggestion

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Billboard AI Backend Running"

@app.route("/scan")
def scan():

    faces = detect_faces()

    add_stat(faces)

    return jsonify({
        "faces_detected": faces
    })


@app.route("/stats")
def stats():
    return jsonify(get_stats())


@app.route("/suggestion")
def suggestion():
    return jsonify({
        "suggestion": get_suggestion()
    })


if __name__ == "__main__":
    app.run(debug=True)