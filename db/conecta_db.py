import psycopg2
from psycopg2.extras import DictCursor

host      = 'containers-us-west-166.railway.app'
user      = 'postgres'
password  = 'LgutXJIlBMGq7bG5HRD2'
database  = 'railway'
port      = 8002

def executa_query(sql, boo_select=False):
    string_conexao = "user={0} password={1} host={2} port={3} dbname={4}".format( user, password, host, port, database)
    conn = psycopg2.connect(string_conexao)
    print("Connection established")

    if(boo_select):
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(sql)
        resultado = cursor.fetchall();

        return resultado
    
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

