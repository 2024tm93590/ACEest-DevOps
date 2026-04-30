from flask import Flask, render_template_string, request, redirect, session
import sqlite3
from datetime import date
import random

app = Flask(__name__)
app.secret_key = "aceest_secret"

DB_NAME = "aceest_fitness.db"

# ---------------- DB ----------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        program TEXT,
        membership_status TEXT
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT,
        date TEXT,
        workout_type TEXT,
        duration TEXT
    )""")

    cur.execute("SELECT * FROM users WHERE username='admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users VALUES ('admin','admin','Admin')")

    conn.commit()
    conn.close()


# ---------------- UI ----------------
login_html = """
<h2>ACEest Login</h2>
<form method="POST">
<input name="username">
<input name="password" type="password">
<button>Login</button>
</form>
"""

dashboard_html = """
<h2>Dashboard</h2>
<p>User: {{user}}</p>

<form method="POST" action="/add_client">
<input name="name" placeholder="Client Name">
<button>Add</button>
</form>

<h3>Clients</h3>
<ul>
{% for c in clients %}
<li>
{{c[1]}} | {{c[2]}}
<a href="/generate/{{c[1]}}">Generate Program</a>
<a href="/workout/{{c[1]}}">Workout</a>
</li>
{% endfor %}
</ul>

<a href="/logout">Logout</a>
"""

workout_html = """
<h2>Workout - {{client}}</h2>
<form method="POST">
<input name="type" placeholder="Type">
<input name="duration" placeholder="Duration">
<button>Save</button>
</form>
"""


# ---------------- ROUTES ----------------
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u,p))
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = u
            return redirect("/dashboard")

    return login_html


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()
    conn.close()

    return render_template_string(dashboard_html, user=session["user"], clients=clients)


@app.route("/add_client", methods=["POST"])
def add_client():
    name = request.form["name"]

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO clients VALUES (NULL, ?, 'None', 'Active')", (name,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")


@app.route("/generate/<name>")
def generate(name):
    programs = ["HIIT", "Strength", "Cardio"]
    prog = random.choice(programs)

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE clients SET program=? WHERE name=?", (prog,name))
    conn.commit()
    conn.close()

    return f"Program: {prog} <br><a href='/dashboard'>Back</a>"


@app.route("/workout/<client>", methods=["GET","POST"])
def workout(client):
    if request.method == "POST":
        t = request.form["type"]
        d = request.form["duration"]

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("INSERT INTO workouts VALUES (NULL,?,?,?,?)",
                    (client, str(date.today()), t, d))
        conn.commit()
        conn.close()

        return redirect("/dashboard")

    return render_template_string(workout_html, client=client)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------- RUN ----------------
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)