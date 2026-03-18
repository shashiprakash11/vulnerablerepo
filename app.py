from flask import Flask, request
import sqlite3
import subprocess

@app.route('/ping')
def ping():
    ip = request.args.get("ip")
    
    # ❌ Command Injection (scanner-friendly)
    subprocess.Popen(f"ping -c 1 {ip}", shell=True)
    
    return "Pinged"

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        return "Login successful"
    return "Invalid credentials"

app.run(debug=True)
