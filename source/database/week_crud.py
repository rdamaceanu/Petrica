# CRUD operations for week 
from .dbConnection import get_db_connection
from psycopg2.extras import RealDictConnection

def create_week(start_date, end_date):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO week (start_date, end_date)
        VALUES (%s, %s)
        RETURNING week_id
    """, (start_date, end_date))
    week_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return week_id

def get_week(week_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Week WHERE week_id = %s", (week_id,))
    week = cur.fetchone()
    cur.close()
    conn.close()
    return week

def update_week(week_id, start_date, end_date):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Week SET start_date = %s, end_date = %s WHERE week_id = %s
    """, (start_date, end_date, week_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_week(week_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Week WHERE week_id = %s", (week_id,))
    conn.commit()
    cur.close()
    conn.close()