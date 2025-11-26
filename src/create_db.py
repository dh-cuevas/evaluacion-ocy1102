# -*- coding: utf-8 -*-
import sqlite3
import hashlib

# Conexion a la base de datos (se creara automaticamente si no existe)
conn = sqlite3.connect('example.db')

# Crear un cursor
c = conn.cursor()

# Crear la tabla de usuarios
c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')

# Funcion para hash de contrasenas
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Insertar un usuario de prueba (las contrasenas estan en SHA256 de 'password')
c.execute('''
    INSERT INTO users (username, password, role) VALUES
    ('admin', ?, 'admin'),
    ('user', ?, 'user')
''', (hash_password('password'), hash_password('password')))

# Crear la tabla de comentarios
c.execute('''
    CREATE TABLE comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        comment TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Guardar los cambios y cerrar la conexion
conn.commit()
conn.close()

print("Database and tables created successfully.")