import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")
APP_NAME = os.getenv("APP_NAME", "flask-ecs-demo")

@app.route("/")
def home():
    return jsonify(message=f"Hello from {APP_NAME}", environment=APP_ENV)

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

# Confirms the secret is loaded without ever exposing it
@app.route("/config")
def config():
    return jsonify(api_key_set=bool(os.getenv("API_KEY")))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)