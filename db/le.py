
def le_st():
    sql = f"""
        select
            nome, numero, peso, altura, local_atua
            from  public.stormtrooper;
    """
    from db.conecta_db import executa_query    
    array_informacoes = executa_query(sql, True)

    return array_informacoes


def get_infos(numero):
    sql = f"""
        select
            nome, numero, peso, altura, local_atua
            from  public.stormtrooper where numero = {numero};
    """
    from db.conecta_db import executa_query    
    array_informacoes = executa_query(sql, True)

    return array_informacoes
