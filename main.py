import binary as binary
from flask import Flask, render_template,  request, redirect, url_for
import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#DATABASE_URL = os.environ.get("DATABASE_URL")
app.config('SQLALCHEMY_DATABASE_URI') = 

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Base url: {DATABASE_URL}"


if __name__ == "__main__":
    app.run()
