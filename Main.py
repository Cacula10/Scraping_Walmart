from Scraping.BeautifulSoup.Beautifulsoup import * # rodando a classe beautifulsoup
from Def.Defs.Colors import *

#from pygame import mixer
#mixer.init()
#mixer.music.load('mortal.mp3')
#mixer.music.play()
#parar = input('Digite ENTER para interromper...')

lista = [[], [], [], []]
prov = []

for i in main_container_note:
    prov.append(i.a.span.text)
    lista[0].append(prov[:])
    prov.clear()

for i in main_container_preco:
    prov.append(i.span.text)
    lista[1].append(prov[:])
    prov.clear()

for i in main_container_star:
    prov.append(i.text)
    lista[2].append(prov[:])
    prov.clear()

for i in main_container_reviews:
    prov.append(i.text)
    lista[3].append(prov[:])
    prov.clear()

# utilizado o metodo zip para organizar lista
aninhado = []
for i in tuple(zip(lista[0], lista[1], lista[2], lista[3])):
    aninhado.append(i)

