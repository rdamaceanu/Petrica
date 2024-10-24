# utilities.py
from database.dbConnection import get_db_connection

def get_days_in_week(week_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM Day WHERE week_id = %s ORDER BY date", (week_id,))
    days = cur.fetchall()
    cur.close()
    conn.close()
    return days

def get_day_parts_in_day(day_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM DayPart WHERE day_id = %s", (day_id,))
    day_parts = cur.fetchall()
    cur.close()
    conn.close()
    return day_parts

def get_minitasks_in_day_part(day_part_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT * FROM MiniTask WHERE day_part_id = %s ORDER BY task_order
    """, (day_part_id,))
    minitasks = cur.fetchall()
    cur.close()
    conn.close()
    return minitasks