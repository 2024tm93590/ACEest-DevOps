import os
import sqlite3
import pytest

from app.ACEest_Fitness import init_db, DB_NAME

def test_basic():
    assert 1 + 1 == 2
# ---------- TEST 1: Database Creation ----------
def test_database_created():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    init_db()

    assert os.path.exists(DB_NAME)


# ---------- TEST 2: Tables Exist ----------
def test_tables_exist():
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    tables = ["users", "clients", "progress", "workouts", "exercises", "metrics"]

    for table in tables:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        assert cur.fetchone() is not None

    conn.close()


# ---------- TEST 3: Default Admin Exists ----------
def test_default_admin():
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username='admin'")
    admin = cur.fetchone()

    assert admin is not None
    assert admin[0] == "admin"

    conn.close()


# ---------- TEST 4: Insert Client ----------
def test_insert_client():
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("INSERT INTO clients (name, membership_status) VALUES (?,?)", ("TestUser", "Active"))
    conn.commit()

    cur.execute("SELECT * FROM clients WHERE name='TestUser'")
    result = cur.fetchone()

    assert result is not None

    conn.close()