from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# La config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todo_app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def index():
    # Pour récupérer toutes les notes depuis la base de données
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()
    return render_template("notes.html", notes=notes)


@app.route("/add_note", methods=["POST"])
def add_note():
    # Pour créer une nouvelle note
    title = request.form["title"]
    content = request.form["content"]
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO notes (title, content, done) VALUES (%s, %s, %s)", (title, content, False))
    mysql.connection.commit()
    return render_template("redirect.html", target_url="/")


@app.route("/api/notes/<int:note_id>/done", methods=["POST"])
def update_note_done(note_id):
    # Pour mettre à jour une note 
    data = request.get_json()
    done = data.get("done", False)
    cur = mysql.connection.cursor()
    cur.execute("UPDATE notes SET done = %s WHERE id = %s", (done, note_id))
    mysql.connection.commit()
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run()
