"""
Main Flask application with proper documentation and code quality
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def hello():
    """
    Main endpoint returning application info

    Returns:
        JSON response with message, version, and status
    """
    version = os.getenv("VERSION", "1.0")
    return jsonify(
        {
            "message": "Hello from Harbor!",
            "version": version,
            "status": "running",
        }
    )


@app.route("/health")
def health():
    """
    Health check endpoint for Kubernetes probes

    Returns:
        JSON response with health status
    """
    return jsonify({"status": "healthy"})


@app.route("/info")
def info():
    """
    Application information endpoint

    Returns:
        JSON response with app details
    """
    return jsonify(
        {
            "app": "my-app",
            "environment": os.getenv("ENV", "production"),
            "version": os.getenv("VERSION", "1.0"),
        }
    )


def calculate_sum(num_a: int, num_b: int) -> int:
    """
    Calculate sum of two numbers

    Args:
        num_a: First number
        num_b: Second number

    Returns:
        Sum of the two numbers
    """
    return num_a + num_b


def calculate_product(num_a: int, num_b: int) -> int:
    """
    Calculate product of two numbers

    Args:
        num_a: First number
        num_b: Second number

    Returns:
        Product of the two numbers
    """
    return num_a * num_b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
