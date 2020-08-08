from Database.Database.Database import cursor, conn
from Scraping.BeautifulSoup.Beautifulsoup import *
from datetime import datetime

first = str(main_container_link[0]).split()
for i in first:
    if 'href' in i:
        Link = i
        break

dicionario = dict()

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
    print('REGISTRO CADASTRADO OU ATUALIZADO NO BANCO')
else:
    print('NÃO VOU ADICIONAR, POIS JA ESTÁ CADASTRADO NO BANCO E TAMBÉM NÃO TIVEMOS ALTERAÇÃO NO PREÇO')