# database/journal_crud.py
from dbConnection import get_db_connection

def save_journal_entry(day_id, content):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Journal (day_id, content)
        VALUES (%s, %s)
        ON CONFLICT (day_id) DO UPDATE SET content = EXCLUDED.content
    """, (day_id, content))
    conn.commit()
    cur.close()
    conn.close()

def get_journal_entry(day_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM Journal WHERE day_id = %s", (day_id,))
    entry = cur.fetchone()
    cur.close()
    conn.close()
    return {'content': entry[0] if entry else ''}
