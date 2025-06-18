from app.extensions import db
from app.models.task import Task
from app.models.category import Category
import uuid

class TaskService:
    @staticmethod
    def create_task(task_data):
        """Create a new task with UUID"""
        required_fields = ['description']
        if not all(field in task_data for field in required_fields):
            raise ValueError(f"Missing required fields: {required_fields}")

        new_task = Task(
            description=task_data['description'],
            category_id=uuid.UUID(task_data['category_id']) if 'category_id' in task_data else None,
            priority=task_data.get('priority', 1),
            completed=task_data.get('completed', False)
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def get_all_tasks():
        """Get all tasks with category relationships"""
        return db.session.query(Task).options(db.joinedload(Task.category)).all()

    @staticmethod
    def get_task_by_id(task_id):
        """Get single task by UUID"""
        return Task.query.get(uuid.UUID(task_id))

    @staticmethod
    def update_task(task_id, update_data):
        """Update existing task"""
        task = Task.query.get(uuid.UUID(task_id))
        if not task:
            raise ValueError("Task not found")

        if 'description' in update_data:
            task.description = update_data['description']
        if 'category_id' in update_data:
            task.category_id = uuid.UUID(update_data['category_id'])
        if 'priority' in update_data:
            task.priority = update_data['priority']
        if 'completed' in update_data:
            task.completed = update_data['completed']

        db.session.commit()
        return task

    @staticmethod
    def delete_task(task_id):
        """Delete a task"""
        task = Task.query.get(uuid.UUID(task_id))
        if not task:
            raise ValueError("Task not found")
        
        db.session.delete(task)
        db.session.commit()

    @staticmethod
    def get_tasks_by_category(category_name):
        """Get tasks filtered by category name"""
        return (db.session.query(Task)
                .join(Category)
                .filter(Category.name == category_name)
                .options(db.joinedload(Task.category))
                .all())

    @staticmethod
    def seed_categories():
        """Initialize default categories"""
        default_categories = ["Health", "Work", "Relationships", "Finance", "Personal Growth"]
        for name in default_categories:
            if not Category.query.filter_by(name=name).first():
                db.session.add(Category(name=name))
        db.session.commit()

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        TaskService.seed_categories()