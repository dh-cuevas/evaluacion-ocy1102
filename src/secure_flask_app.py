from flask import Flask, request, render_template, session, redirect, url_for, escape
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# CORRECCION VULN-004: Secret key fija desde variable de entorno
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production-12345678')

def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

# CORRECCION VULN-005: Eliminada funcion hash_password debil

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        
        # CORRECCION VULN-001: Consulta parametrizada (sin SQL Injection)
        query = "SELECT * FROM users WHERE username = ?"
        user = conn.execute(query, (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error=True)
    
    return render_template('login.html', error=False)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    conn = get_db_connection()
    comments = conn.execute("SELECT comment FROM comments WHERE user_id = ?", (user_id,)).fetchall()
    conn.close()
    
    return render_template('dashboard.html', user_id=user_id, comments=comments)

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # CORRECCION VULN-002: Escape de entrada (XSS)
    comment = escape(request.form['comment'])
    user_id = session['user_id']
    
    conn = get_db_connection()
    conn.execute("INSERT INTO comments (user_id, comment) VALUES (?, ?)", (user_id, comment))
    conn.commit()
    conn.close()
    
    return redirect(url_for('dashboard'))

@app.route('/admin')
def admin():
    if 'user_id' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    return render_template('admin.html')

# CORRECCION VULN-003: Debug mode desactivado
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)