import psycopg2

try:
    conn = psycopg2.connect(
        host="aws-0-ap-southeast-2.pooler.supabase.com",
        port=6543,
        dbname="postgres",
        user="postgres.sbybijjoscjjapfmjfjh",
        password="F9iT86AUnLR0atZG",
        connect_timeout=10,
        keepalives=1,
        keepalives_idle=30,
        sslmode="require"
    )
    print("✅ Raw connection successful!")
except Exception as e:
    print(f"❌ Raw connection failed: {e}")