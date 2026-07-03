import sqlite3
from pathlib import Path


DB_PATH = Path("data/docpilot.db")


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        file_name TEXT NOT NULL,
        file_path TEXT NOT NULL,
        extracted_text_path TEXT,
        summary_path TEXT,
        status TEXT DEFAULT 'DOWNLOADED',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_document(user_id: int, file_name: str, file_path: str):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO documents
        (user_id,file_name,file_path)
        VALUES (?,?,?)
        """,
        (user_id, file_name, file_path),
    )

    conn.commit()
    document_id = cursor.lastrowid
    conn.close()

    return document_id


def update_status(document_id: int, status: str):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE documents
        SET status=?
        WHERE id=?
        """,
        (status, document_id),
    )

    conn.commit()
    conn.close()


def update_output_files(
    document_id: int,
    extracted_text_path: str,
    summary_path: str,
):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE documents
        SET extracted_text_path=?,
            summary_path=?
        WHERE id=?
        """,
        (
            extracted_text_path,
            summary_path,
            document_id,
        ),
    )

    conn.commit()
    conn.close()