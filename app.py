from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def hello():
    version = os.getenv("VERSION", "1.0")
    return jsonify(
        {"message": "Hello from Harbor!", "version": version, "status": "running"}
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/info")
def info():
    return jsonify(
        {
            "app": "my-app",
            "environment": os.getenv("ENV", "production"),
            "version": os.getenv("VERSION", "1.0"),
        }
    )


def calculate_sum(a, b):
    return a + b


def calculate_product(a, b):
    return a * b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
