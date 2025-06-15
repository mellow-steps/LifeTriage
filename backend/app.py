from flask import Flask
app = Flask(__name__)

@app.route('/') 
def hello():
    return "Hello, LifeTriage!"

if __name__ == '__main__':
    app.run(debug=True)

from app.models import create_tables

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
    