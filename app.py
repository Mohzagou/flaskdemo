from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Hoofdpagina")
def Hoofdpagina():
    return "<p>Blog tekst hier invullen!</p>"

@app.route("/ABC/<voornaam>")
def ABC(voornaam):
    return "<p>Welkom : "+voornaam+"!</p>"