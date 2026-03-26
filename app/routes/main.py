import sqlite3
from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

DATABASE = "database.db"

@main_bp.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":
        mood = request.form.get("mood")
        track = request.form.get("track")
        artist = request.form.get("artist")

        print("Mood:", mood)
        print("Track:", track)
        print("by", artist)

    return render_template("form.html")
