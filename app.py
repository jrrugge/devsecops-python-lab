from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    """Return the health status of the application."""
    return jsonify(status="ok"), 200


@app.get("/greet")
def greet():
    """Return a simple greeting using controlled user input."""
    name = request.args.get("name", "world")
    safe_name = name.strip()[:50]

    return jsonify(message=f"Hello, {safe_name}!"), 200


if __name__ == "__main__":
    app.run(debug=False)