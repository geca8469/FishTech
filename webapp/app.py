from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
import db

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=1,
    x_proto=1,
    x_host=1,
    x_prefix=1
)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )