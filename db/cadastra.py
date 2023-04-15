from db.conecta_db import executa_query

def set_maior():
    sql = f"""
        SELECT max(numero)
        FROM public.stormtrooper;
    """
    arrayComMaior = executa_query(sql, True)
    maior = arrayComMaior[0][0]

    if(maior):
        print(maior)
        return maior + 1
    else:
        maior = 1
        return maior   

def cadastra_st(nome, peso, altura, local):
    
    msg = ''

    sql = f"""
        INSERT INTO public.stormtrooper
            (nome, numero, peso, altura, local_atua)
            VALUES('{nome}', {set_maior()}, {peso}, {altura}, '{local}');
    """
    executa_query(sql)
    
    msg = 'cadastrado'

    return msg
