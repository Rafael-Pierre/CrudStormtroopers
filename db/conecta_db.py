import psycopg2

host      = 'containers-us-west-147.railway.app'
user      = 'postgres'
password  = 'yKzfd7b34pPugCB0fssf'
database  = 'railway'
port      = 5608

def executa_query(sql):
    string_conexao = "user={0} password={1} host={2} port={3} dbname={4}".format( user, password, host, port, database)
    conn = psycopg2.connect(string_conexao)
    print("Connection established")

    cursor = conn.cursor()
    comando = sql

    cursor.execute(comando)
    conn.commit()

