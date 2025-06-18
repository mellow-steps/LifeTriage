import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import QueuePool

# Initialize extensions without app context
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load config
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'poolclass': QueuePool,
        'pool_pre_ping': True,
        'pool_recycle': 300,
        'pool_size': 5,
        'max_overflow': 10
    }
    
    # Initialize db with app
    db.init_app(app)
    
    # Import and register blueprints HERE to avoid circular imports
    with app.app_context():
        from app.routes.health import bp as health_bp
        from app.routes.tasks import bp as tasks_bp
        app.register_blueprint(health_bp)
        app.register_blueprint(tasks_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)