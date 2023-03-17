
def edit_st(nome, numero, peso, altura, local):
    
    msg = ''

    sql = f"""
        UPDATE public.stormtrooper
        SET nome='{nome}', altura={altura}, peso={peso}, local_atua='{local}'
        WHERE numero={numero};
    """
    from db.conecta_db import executa_query

    executa_query(sql)
    
    msg = 'editado'

    return msg
