#!/usr/bin/env python3
"""Create a Flask app that has a single GET route ("/")"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def index() -> object:
    """Index"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> object:
    """Users"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify({"message": "email required"}), 400
    if password is None:
        return jsonify({"message": "password required"}), 400
    try:
        AUTH.register_user(email=email, password=password)
    except Exception as Error:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
