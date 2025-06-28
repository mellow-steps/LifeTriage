#!/usr/bin/env python3
"""
Script to verify categories in the database
"""
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.models.category import Category

def main():
    """Verify categories in the database"""
    print("🔍 Checking categories in database...")
    
    app = create_app()
    
    with app.app_context():
        try:
            categories = Category.query.all()
            print(f"📋 Found {len(categories)} categories:")
            
            if categories:
                for category in categories:
                    print(f"   - {category.name} (ID: {category.id})")
            else:
                print("   No categories found in database")
                
        except Exception as e:
            print(f"❌ Error checking categories: {str(e)}")
            return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 