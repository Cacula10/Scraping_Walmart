from Database.Database.Database import cursor, conn
from Scraping.BeautifulSoup.Beautifulsoup import *

dicionario = dict()
dicionario = {'Name': str(main_container_note[0].a.span.text).strip(),
              'Price': str(main_container_preco[0].span.text).strip(),
              'Stars': str(main_container_star[0].text).strip(),
              'Reviews': str(main_container_reviews[0].text).strip()}

cursor.execute("insert into [dbo].[PRODUTOS]"
               "values (?,?,?,?)",
               (dicionario['Name'],
                dicionario['Price'],
                dicionario['Stars'],
                dicionario['Reviews']))
conn.commit()