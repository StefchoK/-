from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Comment, Product, db

comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/products/<int:product_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(product_id):
    data = request.get_json()
    current_user_id = get_jwt_identity()
    if not Product.query.get(product_id):
        return jsonify({'error': 'Product not found'}), 404
    comment = Comment(text=data['text'], user_id=current_user_id, product_id=product_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'message': 'Comment added'}), 201

@comment_bp.route('/products/<int:product_id>/comments', methods=['GET'])
def get_comments(product_id):
    comments = Comment.query.filter_by(product_id=product_id).all()
    return jsonify([{'id': c.id, 'text': c.text, 'user_id': c.user_id} for c in comments])