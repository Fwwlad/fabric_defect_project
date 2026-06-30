import sqlite3
from datetime import datetime

DATABASE_NAME = "history.db"


def init_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            filename TEXT NOT NULL,
            cup_count INTEGER NOT NULL,
            processing_time REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_request(filename, cup_count, processing_time):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO requests (
            timestamp,
            filename,
            cup_count,
            processing_time
        )
        VALUES (?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        filename,
        cup_count,
        processing_time
    ))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            timestamp,
            filename,
            cup_count,
            processing_time
        FROM requests
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows