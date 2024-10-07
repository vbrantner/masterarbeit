from flask import Flask, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(".", path)


if __name__ == "__main__":
    os.makedirs("segments", exist_ok=True)
    app.run(host="0.0.0.0", port=8080)
