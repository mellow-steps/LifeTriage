from flask import Blueprint, jsonify, request
from app.services.task_service import TaskService
from app.models.task import Task
from app.extensions import db

bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@bp.route('/', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    tasks = TaskService.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks]), 200

@bp.route('/', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    
    # Basic validation
    if not data or 'description' not in data:
        return jsonify({"error": "Description is required"}), 400
    
    try:
        task = TaskService.create_task({
            'description': data['description'],
            'category': data.get('category'),
            'priority': data.get('priority', 1)
        })
        return jsonify(task.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<uuid:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task by ID"""
    task = TaskService.get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict()), 200

@bp.route('/<uuid:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a specific task"""
    data = request.get_json()
    try:
        updated_task = TaskService.update_task(task_id, data)
        return jsonify(updated_task.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<uuid:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a specific task"""
    try:
        TaskService.delete_task(task_id)
        return jsonify({"message": "Task deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500