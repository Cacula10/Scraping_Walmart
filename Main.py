from Database.Database.Database import cursor, conn
from Scraping.BeautifulSoup.Beautifulsoup import *

first = str(main_container_link[0]).split()
for i in first:
    if 'href' in i:
        Link = i
        break

dicionario = dict()

dicionario = {'Link': str(Link.strip()),
              'Name': str(main_container_note[0].a.span.text).strip(),
              'Price': str(main_container_preco[0].span.text).strip(),
              'Stars': str(main_container_star[0].text).strip(),
              'Reviews': str(main_container_reviews[0].text).strip()}

cursor.execute("SELECT LINK FROM PRODUTOS")
resultado_link = cursor.fetchone()
resultado_link = str(resultado_link)
cursor.execute("SELECT PRICE FROM PRODUTOS")
resultado_price = cursor.fetchone()
resultado_price = str(resultado_price)

if dicionario["Link"] == resultado_link[2:-4] and dicionario["Price"] == resultado_price[2:-4]:
    print('NÃO VOU ADICIONAR, POIS JA ESTÁ CADASTRADO NO BANCO TAMBÉM E TAMBÉM NÃO TIVEMOS ALTERAÇÃO NO PREÇO DO PRODUTO')
else:
    cursor.close()
    cursor = conn.cursor()
    cursor.execute("insert into [dbo].[PRODUTOS] values (?,?,?,?,?)",
                   (dicionario['Link'],
                    dicionario['Name'],
                    dicionario['Price'],
                    dicionario['Stars'],
                    dicionario['Reviews']))
    conn.commit()
    print('REGISTRO CADASTRADO NO BANCO')