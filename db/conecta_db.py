import psycopg2

host      = 'containers-us-west-147.railway.app'
user      = 'postgres'
password  = 'yKzfd7b34pPugCB0fssf'
database  = 'railway'
port      = 5608

string_conexao = "user={0} password={1} host={2} port={3} dbname={4}".format( user, password, host, port, database)
#string_conexao = 'postgresql://${{postgres}}:${{yKzfd7b34pPugCB0fssf}}@${{containers-us-west-147.railway.app}}:${{5608}}/${{railway}}'
conn = psycopg2.connect(string_conexao)
print("Connection established")

cursor = conn.cursor()

comando = 'select * from stormtrooper'

cursor.execute(comando)

resultado = cursor.fetchall()

rows = len(resultado)

for row in resultado:
    print(row)