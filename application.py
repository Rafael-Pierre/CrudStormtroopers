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

    from db.le import le_st

    dict_informacoes = le_st()
    
    return render_template("home.html",
                            dict_informacoes=dict_informacoes
                        )

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