#!/usr/bin/env python3
"""Create a Flask app that has a single GET route ("/")"""
from flask import Flask, jsonify, request, abort
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> object:
    """implement a login function to respond
    to the POST /sessions route"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        abort(401)
    if AUTH.valid_login(email, password) is True:
        AUTH.create_session(email)
        return jsonify({"email": email, "message": "logged in"})
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
