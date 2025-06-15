from app.utils.database import SessionLocal
from app.models.category import Category

def seed_categories():
    db = SessionLocal()
    default_categories = ["Health", "Work", "Relationships", "Finance", "Personal Growth"]
    for name in default_categories:
        if not db.query(Category).filter_by(name=name).first():
            db.add(Category(name=name))
    db.commit()
    db.close()

if __name__ == "__main__":
 seed_categories()