from sqlalchemy import text

from app.database.connection import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION()"))
        version = result.fetchone()

        print("Connected successfully!")
        print("MySQL Version:", version[0])

except Exception as e:
    print("Database connection failed:", e)