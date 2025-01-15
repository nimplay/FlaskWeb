from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello My friend <h1>PEPE</h1>"

@app.route("/<name>")
def user(name):
    return f"hello {name}"

@app.route("/admin")
def user():
    return redirect(url_for("/"))


if __name__ == "__main__":
    app.run()
