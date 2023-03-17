
def apaga_st(numero):
    sql = f"""
        DELETE FROM public.stormtrooper
        WHERE numero= {numero};
    """
    from db.conecta_db import executa_query    
    array_informacoes = executa_query(sql)

    msg = 'apagado'

    return msg