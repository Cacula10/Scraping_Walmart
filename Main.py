from Database.Database.Database import cursor, conn
from Scraping.BeautifulSoup.Beautifulsoup import *
from datetime import datetime
from Def.Defs.Colors import *

from pygame import mixer
mixer.init()
mixer.music.load('mortal.mp3')
mixer.music.play()
parar = input('Digite ENTER para interromper...')


first = str(main_container_link[0]).split()
for i in first:
    if 'href' in i:
        Link = i
        break

dicionario = {'Link': str(Link.strip()),
              'Date': str(str(datetime.now())),
              'Name': str(main_container_note[0].a.span.text).strip(),
              'Price': str(main_container_preco[0].span.text).strip(),
              'Stars': str(main_container_star[0].text).strip(),
              'Reviews': str(main_container_reviews[0].text).strip()}

cursor.execute("select * from produtos where link = (?)", dicionario["Link"])
all_reg = cursor.fetchall()

if len(all_reg) == 0 or all_reg[-1][3] != dicionario["Price"]:
    cursor = conn.cursor()
    cursor.execute("insert into [dbo].[PRODUTOS] values (?,?,?,?,?,?)",
                   (str(dicionario['Link']),
                    str(dicionario['Date']),
                    str(dicionario['Name']),
                    str(dicionario['Price']),
                    str(dicionario['Stars']),
                    str(dicionario['Reviews'])))
    conn.commit()
    conn.close()
    def_cores('<<< REGISTRO CADASTRADO OU ATUALIZADO NO BANCO >>>', 'azul')
    def_cores('<<< DESCONECTADO SESSÃO DA BASE >>>', 'azul')
else:
    conn.close()
    def_cores('<<< NÃO VOU ADICIONAR, POIS JA ESTÁ CADASTRADO NO BANCO E TAMBÉM NÃO TIVEMOS ALTERAÇÃO NO PREÇO >>>', 'vermelho')
    def_cores('<<<DESCONECTADO SESSÃO DA BASE >>>', 'azul')

