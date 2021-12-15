from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql://root:password@mysql.default/test'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM test.messages', con=db_connection)
print(df)
db_connection.dispose() 