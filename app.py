from flask import Flask, jsonify

app = Flask(__name__)

# ---------- API Version 1 ----------
@app.route("/api/v1/users")
def users_v1():

    return jsonify({
        "version": "v1",
        "users": [
            {
                "id": 1,
                "name": "Kunal"
            },
            {
                "id": 2,
                "name": "Rahul"
            }
        ]
    })


# ---------- API Version 2 ----------
@app.route("/api/v2/users")
def users_v2():

    return jsonify({
        "version": "v2",
        "users": [
            {
                "id": 1,
                "name": "Kunal",
                "email": "kunal@example.com"
            },
            {
                "id": 2,
                "name": "Rahul",
                "email": "rahul@example.com"
            }
        ]
    })


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


# ---------- Home ----------
@app.route("/")
def home():

    return jsonify({
        "message": "API Versioning Demo"
    })


if __name__ == "__main__":
    app.run(debug=True)
