from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Comment, db

comment_bp = Blueprint("comment", __name__)

@comment_bp.route('/<int:product_id>/comments', methods=['GET'])
def get_comments(product_id):
    comments = Comment.query.filter_by(product_id=product_id).all()
    return jsonify([{'id': c.id, 'text': c.text, 'user_id': c.user_id} for c in comments])

@comment_bp.route('/<int:product_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(product_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    comment = Comment(text=data['text'], product_id=product_id, user_id=user_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'message': 'Comment added'})