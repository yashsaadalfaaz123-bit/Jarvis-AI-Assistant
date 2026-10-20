# # name = "Tauseeb"
# # name = "Rahul"
# # # print(name)

# import os
# import json
# import sqlite3

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_FILE = os.path.join(BASE_DIR, "jarvis_memory.db")
# JSON_FILE = os.path.join(BASE_DIR, "memory.json")


# def connect_db():
#     return sqlite3.connect(DB_FILE)


# def setup_memory():
#     with connect_db() as db:
#         db.execute("""
#             CREATE TABLE IF NOT EXISTS chat_history (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_text TEXT NOT NULL,
#                 jarvis_text TEXT NOT NULL,
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             )
#         """)

#         count = db.execute(
#             "SELECT COUNT(*) FROM chat_history"
#         ).fetchone()[0]

#         # Import old chats only when database is empty
#         if count == 0 and os.path.exists(JSON_FILE):
#             try:
#                 with open(JSON_FILE, "r", encoding="utf-8") as f:
#                     memory = json.load(f)

#                 chats = memory.get("chat_history", [])

#                 for chat in chats:
#                     if isinstance(chat, dict):
#                         user_text = chat.get("u", "")
#                         jarvis_text = chat.get("j", "")

#                         if user_text or jarvis_text:
#                             db.execute(
#                                 """INSERT INTO chat_history
#                                 (user_text, jarvis_text)
#                                 VALUES (?, ?)""",
#                                 (str(user_text), str(jarvis_text))
#                             )

#                 print(f"Imported {len(chats)} old chat entries.")

#             except (OSError, json.JSONDecodeError) as e:
#                 print("Old memory import error:", e)


# def save_chat(user_text, jarvis_text):
#     with connect_db() as db:
#         db.execute(
#             """INSERT INTO chat_history (user_text, jarvis_text)
#             VALUES (?, ?)""",
#             (user_text, jarvis_text)
#         )


# def search_chats(query, limit=5):
#     with connect_db() as db:
#         return db.execute(
#             """SELECT user_text, jarvis_text
#             FROM chat_history
#             WHERE user_text LIKE ? OR jarvis_text LIKE ?
#             ORDER BY id DESC LIMIT ?""",
#             (f"%{query}%", f"%{query}%", limit)
#         ).fetchall()


# def chat_count():
#     with connect_db() as db:
#         return db.execute(
#             "SELECT COUNT(*) FROM chat_history"
#         ).fetchone()[0]


# if __name__ == "__main__":
#     setup_memory()
#     print("JARVIS memory ready!")
#     print("Total saved chats:", chat_count())
import os
import json
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "jarvis_memory.db")
JSON_FILE = os.path.join(BASE_DIR, "memory.json")


def connect_db():
    return sqlite3.connect(DB_FILE)


def setup_memory():
    with connect_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_text TEXT NOT NULL,
                jarvis_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        count = db.execute(
            "SELECT COUNT(*) FROM chat_history"
        ).fetchone()[0]

        if count == 0 and os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r", encoding="utf-8") as f:
                memory = json.load(f)

            for chat in memory.get("chat_history", []):
                if isinstance(chat, dict):
                    u = str(chat.get("u", ""))
                    j = str(chat.get("j", ""))
                    if u or j:
                        db.execute(
                            "INSERT INTO chat_history (user_text, jarvis_text) VALUES (?, ?)",
                            (u, j)
                        )


def save_chat(user_text, jarvis_text):
    with connect_db() as db:
        db.execute(
            "INSERT INTO chat_history (user_text, jarvis_text) VALUES (?, ?)",
            (str(user_text), str(jarvis_text))
        )


def search_chats(query, limit=5):
    with connect_db() as db:
        return db.execute(
            """SELECT user_text, jarvis_text FROM chat_history
            WHERE user_text LIKE ? OR jarvis_text LIKE ?
            ORDER BY id DESC LIMIT ?""",
            (f"%{query}%", f"%{query}%", limit)
        ).fetchall()


def chat_count():
    with connect_db() as db:
        return db.execute(
            "SELECT COUNT(*) FROM chat_history"
        ).fetchone()[0]


if __name__ == "__main__":
    setup_memory()
    print("JARVIS memory ready!")
    print("Total saved chats:", chat_count())