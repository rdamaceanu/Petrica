from dbConnection import get_db_connection

def create_day(week_id, date):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Day (week_id, date)
        VALUES (%s, %s)
        RETURNING day_id
    """, (week_id, date))
    day_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return day_id

def get_day(day_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Day WHERE day_id = %s", (day_id,))
    day = cur.fetchone()
    cur.close()
    conn.close()
    return day

def update_day(day_id, week_id, date):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Day SET week_id = %s, date = %s WHERE day_id = %s
    """, (week_id, date, day_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_day(day_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Day WHERE day_id = %s", (day_id,))
    conn.commit()
    cur.close()
    conn.close()