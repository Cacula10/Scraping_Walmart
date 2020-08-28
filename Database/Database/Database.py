import pyodbc
from Def.Defs.Colors import *
try:
    conn = pyodbc.connect("Driver={SQL Server};"
                         "Server=projectwebscraping.cvp5bugirtc4.us-east-2.rds.amazonaws.com,1433;"
                        "Database=Walmart;"
                       "uid=admin;pwd=webscraping"
                      )
    cursor = conn.cursor()
    def_cores('<<< SISTEMA CONECTADO NA BASE COM SUCESSO >>>', 'azul')
    print('')
except:
    def_cores('<<<ERRO AO ACESSAR A BASE >>>', 'vermelho')

#Acesso a Base SQL
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-PO9B1G7;'
#                       'Database=Walmart;'
#                      'Trusted_Connection=yes;')
# cursor = conn.cursor()

#Acesso a base RDS AWS