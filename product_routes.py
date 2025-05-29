from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Product, db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'title': p.title, 'description': p.description, 'user_id': p.user_id} for p in products])

@product_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    new_product = Product(title=data['title'], description=data.get('description'), user_id=current_user_id)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created'}), 201

@product_bp.route('/products/<int:product_id>', methods=['PATCH'])
@jwt_required()
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    current_user_id = get_jwt_identity()
    if product.user_id != current_user_id:
        return jsonify({'error': 'Not allowed'}), 403
    data = request.get_json()
    product.title = data.get('title', product.title)
    product.description = data.get('description', product.description)
    db.session.commit()
    return jsonify({'message': 'Product updated'})

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    current_user_id = get_jwt_identity()
    if product.user_id != current_user_id:
        return jsonify({'error': 'Not allowed'}), 403
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})