import psycopg2

host      = 'localhost'
user      = 'postgres'
password  = 'crud123'
database  = 'postgres'

string_conexao = "host={0} user={1} dbname={2} password={3}".format(host, user, database, password)
conn = psycopg2.connect(string_conexao)
print("Connection established")

cursor = conn.cursor()

comando = 'select * from stormtrooper where numero = 1;'

cursor.execute(comando)

resultado = cursor.fetchall()

rows = len(resultado)

for row in resultado:
    print(row)