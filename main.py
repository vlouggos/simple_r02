import binary as binary
from flask import Flask, render_template,  request, redirect, url_for
import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#DATABASE_URL = os.environ.get("DATABASE_URL")
app.config('SQLALCHEMY_DATABASE_URI') = postgres://dnmfcrwhuxbdpw:16516902f9e5a3cce0305ae4258177d6be7fd060c4e5dbd5740bfc7ba571755f@ec2-52-30-67-143.eu-west-1.compute.amazonaws.com:5432/d17512vorjj707

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Base url: {DATABASE_URL}"


if __name__ == "__main__":
    app.run()
