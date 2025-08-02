from flask import Blueprint,request,jsonify
from models import user_model 
from utils.auth import hash_password,verify_password
from utils.validators import validate_user_data

user_bp=Blueprint('user_route',__name__)
@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = user_model.get_all_users()
    return jsonify([dict(user) for user in users])

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_model.get_user_by_id(user_id)
    if user:
        return jsonify(dict(user))
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    is_valid, msg = validate_user_data(data)
    if not is_valid:
        return jsonify({"error": msg}), 400
    user_model.create_user(data['name'], data['email'], hash_password(data['password']))
    return jsonify({"message": "User created successfully!"}), 201

    
@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    is_valid, msg = validate_user_data(data, require_password=False)
    if not is_valid:
        return jsonify({"error": msg}), 400

    if not user_model.get_user_by_id(user_id):
        return jsonify({"error": "User not found"}), 404

    user_model.update_user(user_id, data['name'], data['email'])
    return jsonify({"message": "User updated successfully"})

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if not user_model.get_user_by_id(user_id):
        return jsonify({"error": "User not found"}), 404

    user_model.delete_user(user_id)
    return jsonify({"message": f"User {user_id} deleted successfully"})

@user_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Name parameter is required"}), 400

    users = user_model.search_users_by_name(name)
    return jsonify([dict(user) for user in users])

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and Password are required"}), 400

    user = user_model.get_user_by_email(email)
    if user and verify_password(user['password'], password):
        return jsonify({"status": "success", "user_id": user['id']})
    else:
        return jsonify({"status": "failed"}), 401