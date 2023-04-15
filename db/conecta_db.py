import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")
port = os.getenv("port")

def executa_query(sql, boo_select=False, debug=False):
    string_conexao = "user={0} password={1} host={2} port={3} dbname={4}".format( user, password, host, port, database)
    conn = psycopg2.connect(string_conexao)
    print("Connection established")

    if(debug):
        print(sql)

    if(boo_select):
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(sql)
        resultado = cursor.fetchall()

        return resultado
    
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

