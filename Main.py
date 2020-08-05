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
              'Reviews': str(main_container_reviews[0].text).strip(),
              'New_Price': str(''),
              'Old_Price': str(''),
              'New_Date': str(''),
              'Old_Date': str('')}

cursor.execute("SELECT LINK FROM PRODUTOS")
resultado_link = cursor.fetchone()
resultado_link = str(resultado_link)

cursor.execute("SELECT PRICE FROM PRODUTOS")
resultado_price = cursor.fetchone()
resultado_price = str(resultado_price)

if len(resultado_link) <= 4:
    cursor = conn.cursor()
    cursor.execute("insert into [dbo].[PRODUTOS] values (?,?,?,?,?,?,?,?,?,?)",
                   (dicionario['Link'],
                    dicionario['Date'],
                    dicionario['Name'],
                    dicionario['Price'],
                    dicionario['Stars'],
                    dicionario['Reviews'],
                    dicionario['New_Price'],
                    dicionario['Old_Price'],
                    dicionario['New_Date'],
                    dicionario['Old_Date']))
    conn.commit()
    print('REGISTRO CADASTRADO NO BANCO')
elif dicionario["Link"] == resultado_link[2:-4] and dicionario["Price"] == resultado_price[3:-4]:# para testar mudo para 3:4
        print('NÃO VOU ADICIONAR, POIS JA ESTÁ CADASTRADO NO BANCO E TAMBÉM NÃO TIVEMOS ALTERAÇÃO NO PREÇO')
elif dicionario["Link"] == resultado_link[2:-4] and dicionario["Price"] != resultado_price[3:-4]:# para testar mudo para 3:4
    cursor = conn.cursor()
    cursor.execute("UPDATE PRODUTOS SET NEW_PRICE = (?) WHERE (?) = (?)", dicionario["Price"], str(dicionario["Link"]), str(dicionario["Link"]))
    cursor.execute("update produtos set Old_Price = (?) where (?) = (?)", dicionario["Price"], str(dicionario["Link"]), str(dicionario["Link"]))
    cursor.execute("update produtos set Price = NEW_PRICE where (?) = (?)", str(dicionario["Link"]), str(dicionario["Link"]))

    cursor.execute("UPDATE PRODUTOS SET NEW_DATE = (?) WHERE (?) = (?)", str(datetime.now()), str(dicionario["Link"]), str(dicionario["Link"]))
    cursor.execute("update produtos set Old_Date = date where (?) = (?)", str(dicionario["Link"]), str(dicionario["Link"]))
    cursor.execute("update produtos set Date = New_Date where (?) = (?)", str(dicionario["Link"]), str(dicionario["Link"]))
    conn.commit()
    print('ATUALIZADO O PREÇO E A DATA')



