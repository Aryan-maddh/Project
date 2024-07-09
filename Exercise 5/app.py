from flask import Flask, request, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = 'submissions.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    db = get_db()
    db.execute('INSERT INTO submissions (name, email) VALUES (?, ?)', (name, email))
    db.commit()
    return f"Name: {name}, Email: {email}"

@app.route('/submissions')
def submissions():
    db = get_db()
    cur = db.execute('SELECT name, email FROM submissions')
    submissions = cur.fetchall()
    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
