import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')

# CORRECCION: Hash seguro con werkzeug (bcrypt)
c.execute('''
    INSERT INTO users (username, password, role) VALUES
    ('admin', ?, 'admin'),
    ('user', ?, 'user')
''', (generate_password_hash('password'), generate_password_hash('password')))

c.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        comment TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

conn.commit()
conn.close()

print("Database and tables created successfully with secure password hashing.")