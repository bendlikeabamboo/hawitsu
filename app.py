from flask import Flask
from dotenv import load_dotenv


dotenv_path = "./"  # Path to .env file
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page. <h1>Hello World<h1>"

@app.route("/name")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()

