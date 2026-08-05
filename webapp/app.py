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
    


### TESTING ROUTES
@app.route('/create_tables')
def create_tables():
    return db.create_tables()

@app.route('/show_table/<table_name>')
def show_table(table_name):
    return db.get_table(table_name)

@app.route('/add_user')
def add_user():
    return db.add_user('name', 'pass')

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )