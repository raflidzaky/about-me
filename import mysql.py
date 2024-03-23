import mysql.connector as connection
import pandas as pd

# Connect to the MySQL connector
db = connection.connect(host='127.0.0.1', 
                        database='bank', 
                        user='user', # Change 'user' and 'password' onto your own database context
                        passwd='password',
                        auth_plugin='mysql_native_password',
                        )

def get_the_data(database):
    try:
        sql = 'SELECT * FROM account'
        df = pd.read_sql(sql, con=database)
        df.to_excel('bank_account.xlsx', 
                     index=False)
        print('Success!')
    except Exception as e:
        print(f'Error!: {e}')

get_the_data(database=db)
