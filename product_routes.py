from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Product, db

product_bp = Blueprint("product", __name__)

@product_bp.route('', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {'id': p.id, 'title': p.title, 'description': p.description, 'user_id': p.user_id}
        for p in products
    ])

@product_bp.route('', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    user_id = get_jwt_identity()
    product = Product(title=data['title'], description=data.get('description'), user_id=user_id)
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created'})

@product_bp.route('/<int:product_id>', methods=['PATCH'])
@jwt_required()
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if product.user_id != get_jwt_identity():
        return jsonify({'error': 'Not allowed'}), 403
    data = request.get_json()
    product.title = data.get('title', product.title)
    product.description = data.get('description', product.description)
    db.session.commit()
    return jsonify({'message': 'Product updated'})

@product_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    if product.user_id != get_jwt_identity():
        return jsonify({'error': 'Not allowed'}), 403
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})