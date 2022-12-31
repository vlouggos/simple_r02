from flask import Flask, render_template
import os
import psycopg2
from flask-sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config('SQLALCHEMY_DATABASE_URI') = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
