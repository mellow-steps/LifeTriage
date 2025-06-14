from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

def init_db():
    # Delete existing database to start fresh
    if os.path.exists('tasks.db'):
        os.remove('tasks.db')
        print("Deleted old database")
    
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database and table created successfully")

@app.route('/')
def home():
    return 'Life Triage Backend'

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        task = request.json.get('task')
        print(f"Received task: {task}")
        try:
            cursor.execute('INSERT INTO tasks (description) VALUES (?)', (task,))
            conn.commit()
            print("Task saved successfully")
            return jsonify({'status': 'Task saved'})
        except Exception as e:
            print(f"Error saving task: {e}")
            return jsonify({'error': str(e)}), 500
        finally:
            conn.close()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)