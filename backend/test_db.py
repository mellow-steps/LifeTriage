from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv('DATABASE_URL')

# Verify the loaded URL
print(f"Connecting to: {DB_URL.split('@')[1].split('/')[0]}") 

engine = create_engine(
    DB_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    echo=True  # Enable SQL logging for debugging
)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        print("✅ SQLAlchemy connection successful!")
        print("PostgreSQL version:", result.scalar())
except Exception as e:
    print(f"❌ SQLAlchemy connection failed: {str(e)}")