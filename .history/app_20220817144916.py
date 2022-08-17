from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Zichtbaar")
    return "<p>Hello, World!</p>"