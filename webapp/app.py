from flask import Flask, render_template, session, request, redirect, jsonify
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
    fish_list = db.get_fish()
    return render_template("fish-collection.html", fish_list=fish_list)

@app.route("/map")
def map_view():
    water_bodies = db.get_water_bodies() or []
    locations = [
        {
            'id': wb[0],
            'name': wb[1],
            'type': wb[2],
            'lat': float(wb[3]) if wb[3] is not None else None,
            'lng': float(wb[4]) if wb[4] is not None else None,
            'size': float(wb[5]) if wb[5] is not None else None,
            'description': wb[6],
        }
        for wb in water_bodies
    ]
    return render_template("map.html", locations=locations)

@app.route("/api/waterbody/<int:waterbody_id>/fish")
def waterbody_fish(waterbody_id):
    fish = db.get_fish_by_waterbody(waterbody_id) or []
    return jsonify([
        {
            'id': f[0],
            'name': f[1],
            'image': f[2],
            'size': float(f[3]) if f[3] is not None else None,
            'description': f[4],
        }
        for f in fish
    ])


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


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result, message = db.add_user(username, password)
        if result:
            return redirect('/login')
        else:
            return render_template('create_account.html', error=message)

    return render_template('create_account.html')



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

@app.route("/seed-db")
def seed_db():
    return db.seed_database()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )