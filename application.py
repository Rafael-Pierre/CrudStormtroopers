from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

from db.le import le_st, get_infos
from db.apaga import apaga_st

@app.route('/', methods=["GET", "POST"])
def tela_inicial():
    return render_template("index.html")



@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template("login.html")



@app.route('/home', methods=["GET", "POST"])
def home():
    dict_informacoes = le_st()
    return render_template("home.html", dict_informacoes=dict_informacoes)

@app.route('/home/apaga<numero>', methods=["GET", "POST"])
def get_number_apaga(numero):
    dict_informacoes = le_st()

    dict_infos = get_infos(numero)
    pk_apaga_numero = dict_infos[0]["numero"]
    return render_template("home.html", pk_apaga_numero=pk_apaga_numero, dict_informacoes=dict_informacoes)

@app.route('/home/edita<numero>', methods=["GET", "POST"])
def get_number_edita(numero):
    dict_informacoes = le_st()

    dict_infos = get_infos(numero)
    pk_edita_numero = dict_infos[0]["numero"]
    return render_template("home.html", pk_edita_numero=pk_edita_numero, dict_informacoes=dict_informacoes, dict_infos=dict_infos)



@app.route('/delete/<numero>', methods=["GET", "POST"])
def delete(numero):
    apaga_st(numero)
    return redirect('/home')

@app.route('/edit', methods=["GET", "POST"])
def edit():
    nome     = request.form.get('nome')
    numero   = request.form.get('numero')
    peso     = request.form.get('peso')
    altura   = request.form.get('altura')
    local    = request.form.get('local')

    from db.edita import edit_st
    edit_st(nome, numero, peso, altura, local)

    return jsonify({"success": True})



@app.route('/cadastra', methods=["GET", "POST"])
def cadastra():
    operacao = request.form.get('operacao')
    nome     = request.form.get('nome')
    numero   = request.form.get('numero')
    peso     = request.form.get('peso')
    altura   = request.form.get('altura')
    local    = request.form.get('local')
    
    if operacao == 'cad':
        from db.cadastra import cadastra_st
        return cadastra_st(nome, numero, peso, altura, local)

    return render_template("cadastra.html")

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run()