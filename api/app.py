from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Since Vercel doesn't support SQLite persistence, we'll use a simple in-memory solution
# or you'd need to use a cloud database like PostgreSQL, MongoDB, etc.
tasks_storage = []

@app.route('/')
def home():
    return 'Life Triage Backend'

@app.route('/api')
def api_home():
    return 'Life Triage API'

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    global tasks_storage
    
    if request.method == 'POST':
        task = request.json.get('task')
        print(f"Received task: {task}")
        try:
            # Add task to in-memory storage
            task_data = {
                'id': len(tasks_storage) + 1,
                'description': task,
                'created_at': 'now'  # You could use datetime here
            }
            tasks_storage.append(task_data)
            print("Task saved successfully")
            return jsonify({'status': 'Task saved'})
        except Exception as e:
            print(f"Error saving task: {e}")
            return jsonify({'error': str(e)}), 500

    return jsonify({'tasks': tasks_storage})

# This is required for Vercel
if __name__ == '__main__':
    app.run()

# Export the app for Vercel
app = app