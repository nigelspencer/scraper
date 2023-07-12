import pyodbc

# Connection details
server = '192.168.1.40\INVESTMENT'
database = 'Finances'
username = 'sa'
password = 'Lucas030599'

# Establishing the connection
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

# Creating a cursor object
cursor = conn.cursor()

# Execute a sample query
cursor.execute('SELECT * FROM etf')

# Fetching and printing the results
for row in cursor:
    print(row)

# Closing the connection
conn.close()
