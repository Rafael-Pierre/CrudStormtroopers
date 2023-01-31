from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def tela_inicial():
    return render_template("index.html")

@app.route('/login')
def tela_login():
    return render_template("login.html")

@app.route('/exibe_stp')
def tela_exibe():
    return render_template("exibe.html")


