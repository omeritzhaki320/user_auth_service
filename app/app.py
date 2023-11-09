from flask import request, jsonify
from pymysql import IntegrityError

from db import app
from models import User, db


@app.route("/register", methods=["POST"])
def register_user():
    user_data = request.json

    username = user_data.get("username")
    password = user_data.get("password")
    email = user_data.get("email")
    full_name = user_data.get("full_name")

    # Check if the username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    new_user = User(username=username, password=password, email=email, full_name=full_name)
    db.session.add(new_user)

    try:
        db.session.commit()
        return jsonify({"message": "User registered successfully", "user_data": user_data}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "User registration failed due to a database error"}), 500


@app.route("/login", methods=["POST"])
def login():
    user_credentials = request.json
    username = user_credentials.get("username")
    password = user_credentials.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({"message": "User logged in successfully", "user_credentials": user_credentials})


@app.route("/profile/<username>", methods=["GET"])
def get_user_profile(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({"username": user.username, "email": user.email, "full_name": user.full_name})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
