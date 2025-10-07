#!/usr/bin/python3
"""This module creates a mini server"""


from flask import Flask, request, jsonify


app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return jsonify('OK')

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)    
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400
    
    username = data['username']
    users[username] = data
    return jsonify({'message': 'User added', 'user': data}), 201

if __name__ == "__main__": 
    app.run(debug=True)