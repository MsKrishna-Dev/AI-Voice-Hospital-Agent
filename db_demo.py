from __future__ import annotations

from sqlalchemy import text

from database import engine #, init_db

def run_sql(query: str) :
    """Run a raw SQL query against the database."""
    """Example:
       rows = run_sql("SELECT * FROM appointments")
       print(rows)
    """
    # init_db()
    with engine.begin() as connection:
        result = connection.execute(text(query))
        return result.fetchall() if result.returns_rows else result.rowcount
    
query = """SELECT * FROM appointments"""
print(run_sql(query))