def cadastra_st(nome, numero, peso, altura, local):
    
    msg = ''

    sql = f"""
        INSERT INTO public.stormtrooper
            (nome, numero, peso, altura, local_atua)
            VALUES('{nome}', {numero}, {peso}, {altura}, '{local}');
    """
    from db.conecta_db import executa_query

    executa_query(sql)
    
    msg = 'cadastrado'

    return msg
