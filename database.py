import sqlite3

def get_db_connection(db_path='tickets.db'):
    conn = sqlite3.connect(db_path)
    return conn

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table structure
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        requestor_seniority INTEGER,
        it_owner TEXT,
        filed_against TEXT,
        ticket_type TEXT,
        severity INTEGER,
        priority INTEGER,
        days_open INTEGER,
        sentiment TEXT,
        description TEXT,
        created_at TEXT
    )
    ''')
    conn.commit()
    conn.close()
