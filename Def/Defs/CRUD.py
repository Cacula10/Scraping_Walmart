from Database.Database.Database import cursor, conn #rodando a clase para conectar na base
from Main import *# rodando a classe principal que organiza meus containers


def crud():
    for i, v in enumerate(aninhado):
        from datetime import datetime
        cursor.execute("insert into [dbo].[PRODUTOS] values (?,?,?,?,?)",
                       (str(v[0][0]),
                        float(v[1][0][1:]),
                        str(v[2][0]),
                        str(v[3][0]),
                        str(datetime.now())))
        conn.commit()
        cursor.execute("delete from PRODUTOS_NOVOS")
        conn.commit()
        cursor.execute("INSERT INTO PRODUTOS_NOVOS select * from [dbo].[vw_ultimo_registro]")
        conn.commit()