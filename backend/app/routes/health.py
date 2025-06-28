from flask import Blueprint
from sqlalchemy import text
from app.extensions import db  # Changed import location

bp = Blueprint('health', __name__)

@bp.route('/health')
def health_check():
    return "OK", 200

@bp.route('/health/db')
def db_check():
    try:
        result = db.session.execute(text("SELECT version()"))
        return {"status": "healthy", "db_version": result.scalar()}, 200
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}, 500
    
#resulting routes
#http://localhost:5000/health
#http://localhost:5000/health/db    

