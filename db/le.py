def le_st():
    
    msg = ''

    sql = f"""
        select
            nome, numero, peso, altura, local_atua
            from  public.stormtrooper;
    """
    from db.conecta_db import executa_query

    executa_query(sql)
    
    msg = 'cadastrado'

    return msg