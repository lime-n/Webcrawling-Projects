from sqlalchemy import create_engine, String
import pandas as pd
import pyodbc
import logging
from itemadapter import is_item
from itemadapter import ItemAdapter

logger = logging.getLogger(__name__)

class DataframeSQLPipelineInject:

    def __init__(self, user, passw, host, port, database, table, if_exists, drivername):
        self._user = user
        self._passw = passw
        self._host = host
        self._port = port
        self._database = database
        self.table = table
        self.if_exists = if_exists
        self.drivername = drivername

    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user = crawler.settings.get('DATABASE')['user'],
            passw = crawler.settings.get('DATABASE')['passw'],
            host = crawler.settings.get('DATABASE')['host'],
            port = crawler.settings.get('DATABASE')['port'],
            database = crawler.settings.get('DATABASE')['database'],
            table = crawler.settings.get('DATABASE')['table'],
            if_exists = crawler.settings.get('DATABASE')['if_exists'],
            drivername = crawler.settings.get('DATABASE')['drivername']
        )

    def open_spider(self, spider): 
        self.engine = create_engine(
            f'{self.drivername}://' + #change this to your required server
            self._user + ':' + 
            self._passw + '@' + 
            self._host + ':' + 
            str(self._port) + '/' + 
            self._database  ,#+f'?driver=ODBC+Driver+18+for+SQL+Server' , #change this to your required driver
            echo=False,
            #connect_args={"timeout":30},
                            pool_pre_ping=True)

        self.conn = self.engine.connect()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self,item, spider):
        if is_item(item):
            table_df = pd.DataFrame([ItemAdapter(item).asdict()])
            print(table_df.dtypes)
            table_df.to_sql(self.table, con=self.engine,method='multi',dtype={'name':String(), 'keyword':String()}, chunksize=2000, index=False, if_exists = self.if_exists)
        else:
            logger.error(f'You need a dict for item, you have type: {type(item)}')

        
