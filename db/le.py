
def le_st():
    
    msg = ''

    sql = f"""
        select
            nome, numero, peso, altura, local_atua
            from  public.stormtrooper;
    """
    from conecta_db import executa_query

    executa_query(sql, True)
    
    array_informacoes = executa_query(sql, True)

    return array_informacoes
