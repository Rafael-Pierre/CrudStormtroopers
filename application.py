from flask import Flask

app = Flask(__name__)

@app.route('/')
def tela_inicial():
    return "Hello world! teste"