from flask import Flask, send_from_directory
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=ROOT, static_url_path="")

@app.route("/")
def index():
    return send_from_directory(ROOT, "Everywatch_CEO_Dashboard_RELEASE.html")

@app.route("/health")
def health():
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))