from flask import Flask, render_template, request, redirect, url_for

import psycopg2

 

app = Flask(__name__)

 

# Database connection

DB_HOST = "localhost"

DB_NAME = "day10"

DB_USER = "postgres"

DB_PASS = "roots"

 

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=5433)

cur = conn.cursor()

 

@app.route('/')

def home():

    return render_template('login.html')

 

@app.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

       

        # Insert user data into the database

        cur.execute("INSERT INTO users1 (username, password) VALUES (%s, %s)", (username, password))

        conn.commit()

       

        return redirect(url_for('dashboard'))

    return render_template('login.html')

 

@app.route('/dashboard')

def dashboard():

    return "Welcome to the Flask!"

 

if __name__ == '__main__':

    app.run(debug=True)
