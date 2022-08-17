from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Zichtbaar")
    print("een extra zin")
    return "<p>Hello, World!</p>"