from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database configuration
db_host = 'mysql-db'
db_user = 'user1'
db_password = 'simrathuser1'
db_name = 'logintest'

# Database connection
db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check credentials in the database
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return render_template('logged_in.html', username=username)
    else:
        return "Invalid credentials. Please try again."

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form['username']
    password = request.form['password']

    # Insert new user into the database
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cursor.execute(query)
    db.commit()

    return f"User {username} successfully registered!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
