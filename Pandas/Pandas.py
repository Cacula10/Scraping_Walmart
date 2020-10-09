import pandas as pd
from Database.Database.Database import conn

# criando um modelo do Banco de dados para o dataset com Pandas
cursor = conn.cursor()
cursor.execute("select * from produtos")
all_reg = cursor.fetchall()

notebook = []
price = []
star = []
reviews = []
data_inserida = []

for i, v in enumerate(all_reg):
    notebook.append(v[0])
    price.append(v[1])
    star.append(v[2])
    reviews.append(v[3])
    data_inserida.append(v[4])


frame_principal = pd.DataFrame({'notebook': notebook,
                      'price': price,
                      'star': star,
                      'reviews': reviews,
                       'data_inserida': data_inserida})

print(frame_principal.head())
