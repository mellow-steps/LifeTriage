#!/usr/bin/env python3
"""
Script to seed the database with default categories
"""
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.services.task_service import TaskService

def main():
    """Run the category seeding"""
    print("🌱 Starting category seeding...")
    
    app = create_app()
    
    with app.app_context():
        try:
            TaskService.seed_categories()
            print("✅ Categories seeded successfully!")
            
            # Verify the categories were created
            from app.models.category import Category
            categories = Category.query.all()
            print(f"📋 Found {len(categories)} categories:")
            for category in categories:
                print(f"   - {category.name}")
                
        except Exception as e:
            print(f"❌ Error seeding categories: {str(e)}")
            return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 