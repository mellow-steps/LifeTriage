from flask import Blueprint, jsonify
from app.models.category import Category
from app.services.task_service import TaskService
from app.extensions import db

bp = Blueprint('categories', __name__, url_prefix='/api/categories')

@bp.route('/', methods=['GET'])
def get_categories():
    """Get all categories"""
    try:
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/seed', methods=['POST'])
def seed_categories():
    """Seed default categories"""
    try:
        TaskService.seed_categories()
        categories = Category.query.all()
        return jsonify({
            "message": "Categories seeded successfully",
            "categories": [category.to_dict() for category in categories]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500 