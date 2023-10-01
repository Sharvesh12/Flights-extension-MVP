import config
import sqlalchemy
from sqlalchemy.pool import NullPool
from sqlalchemy.engine import url as sa_url
from config import logging
import pandas as pd
import os
from datetime import date
from dateutil.relativedelta import relativedelta
from urllib.parse import quote_plus
from sqlalchemy import create_engine
logger = logging.getLogger(__name__)

class DBManager:
    def __init__(self, credentials: dict):
        '''
        :param credentials: dictionary holding username and password for connection
        '''
        port=credentials['port']
        host=credentials['host']
        database=credentials['database']
        username=credentials['username']
        password=quote_plus(credentials['password'])
        self.connection=create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}?schema=public')
        logger.info('CONNECTED')        

    def run_query(self, query_file_name:str, params=None) -> pd.DataFrame:
        '''
        :param query_file_name: name of the file in same directory that holds PG SQL text
        :return: pandas DataFrame
        '''
        with open(f'{config.working_dir}/queries/{query_file_name}.sql','r') as query_file:
            query_text=query_file.read()
            
            logger.info(f'Running Query {query_file_name}')
            df=pd.read_sql_query(sql=query_text, con=self.connection)
            logger.info(f'Execution Completed')
        return df


    def run_etl_query(self, query_file_name:str)->None:
        '''
        :param query_file_name: name of the file in same directory that holds PG SQL DDL
        :return: None
        '''
        with open(f'{config.working_dir}/queries/{query_file_name}.sql','r') as query_file:
            query_text=query_file.read()
            logger.info(f'Running DDL Query {query_file_name}')
            self.connection.execute(query_text)
        logger.info(f'Execution Completed')
        


    def create_table_from_df(self, df:pd.DataFrame, table_name:str) -> None:
        '''
        :param query_file_name: pandas datagrame supposed to be written to DB table
        :return: void
        '''
        df.to_sql(table_name,con=self.connection, index=False, if_exists='append')
        logger.info(f'Dumped to DB')
