import sqlite3
from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

DATABASE = "database.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        mood TEXT,
        track TEXT,
        artist TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@main_bp.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":
    mood = request.form.get("mood")
    track = request.form.get("track")
    artist = request.form.get("artist")

    if not mood or not track:
        return render_template("form.html")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO entries (date, mood, track, artist)
    VALUES (datetime('now'), ?, ?, ?)
    """, (mood, track, artist))

    conn.commit()
    conn.close()

    return render_template("form.html")
