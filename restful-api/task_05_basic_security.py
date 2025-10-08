from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'whatisthis'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if username in users and \
        check_password_hash(user['password'], password):
            return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return 'Basic Auth: Access Granted'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = users.get(username)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    password_is_correct = check_password_hash(user['password'], password)
    if not password_is_correct:
        return jsonify({'error': 'Incorrect password'}), 401
    
    identity_info ={
        'username': username, 
        'role': user['role']
    }
    if not identity_info:
        return jsonify({"error": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=identity_info)

    return jsonify({'access_token': access_token}), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return 'JWT Auth: Access Granted'



@app.route('/admin-only')
@auth.login_required(role='admin')
def admin_access():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify ({'error': 'Admin access required'}), 403
    return 'Admin Access: Granted'

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()