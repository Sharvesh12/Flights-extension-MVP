import config
from config import logging
import pandas as pd
import os
from datetime import date
from dateutil.relativedelta import relativedelta
from urllib.parse import quote_plus
logger = logging.getLogger(__name__)
import psycopg2
import pandas as pd

class DBManager:

    def __init__(self, credentials):
        
        self.connection = psycopg2.connect(
            host=credentials['host'],
            database=credentials['database'], 
            user=credentials['username'],
            password=credentials['password']
        )
        
        print('Connected!')
        
    def run_query(self, query):
        
        df = pd.read_sql(query, self.connection)
        
        return df
    
    def run_ddl_query(self, query):
        
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        
        print('Query executed!')
        
    def create_table_from_df(self, df, table_name):
      
        df.to_sql(name=table_name, con=self.connection, 
                  index=False, if_exists='append')
      
        print('Table created!')
