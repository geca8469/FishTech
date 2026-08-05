from flask import Flask, render_template, session, request, redirect
from werkzeug.middleware.proxy_fix import ProxyFix
import db

app = Flask(__name__)
app.secret_key = 'a secret key'

app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=1,
    x_proto=1,
    x_host=1,
    x_prefix=1
)

### WEB ROUTES
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/fish-collection")
def fish_collection():
    return render_template("fish-collection.html")
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.get_user(username, password)

        if user:
            session['userID'] = user[0]
            session['username'] = user[1]
            return redirect('/')

        else:
            return render_template('login.html', error='Invalid Username or Password')

    return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop('userID', None)
    session.pop('username', None)
    return redirect('/')

### TESTING ROUTES
@app.route('/create_tables')
def create_tables():
    return db.create_tables()

@app.route('/show_table/<table_name>')
def show_table(table_name):
    return db.get_table(table_name)

@app.route('/add_user/<username>/<password>')
def add_user(username, password):
    return db.add_user(username, password)

@app.route('/drop_all_tables')
def drop_all_tables():
    return db.drop_all_tables()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )