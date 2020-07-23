import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-PO9B1G7;'
                      'Database=Walmart;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()