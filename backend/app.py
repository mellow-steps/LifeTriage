from flask import Flask
app = Flask(__name__)
    
@app.route("/api/test-db")
def test_db():
    from app.utils.database import SessionLocal
    from app.models.category import Category
    db = SessionLocal()
    categories = db.query(Category).all()
    db.close()
    return {"categories": [c.name for c in categories]}

from app.models import create_tables

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
    