from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def tela_inicial():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/cadastra', methods=["GET", "POST"])
def cadastra():
    print('entrei')

    nome   = request.form.get('nome')
    numero = request.form.get('numero')
    peso   = request.form.get('peso')
    altura = request.form.get('altura')
    local  = request.form.get('local')
    print(nome)
    print(numero)
    print(peso)
    print(altura)
    print(local)
    return render_template("cadastra.html")

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    return render_template("sobre.html")

