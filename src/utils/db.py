import psycopg
from .logger import logger
from .cli_args import args
from .env import env_value

DB_HOST = env_value('DB_HOST')
DB_PORT = env_value('DB_PORT')
DB_USER = env_value('DB_USER')
DB_PASSWORD = env_value('DB_PASSWORD')
DB_NAME = env_value('DB_NAME')
DB_CONNECTION = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

class DB:
    __connection = None

    @classmethod
    def connection(self) -> psycopg.Connection:
        if not self.__connection:
            logger.debug(f'DB connect "{DB_CONNECTION}"')
            self.__connection = psycopg.connect(DB_CONNECTION)
        return self.__connection

    @classmethod
    def cursor(self) -> psycopg.Cursor:
        return self.connection().cursor()

    @classmethod
    def commit(self):
        return self.connection().commit()

    @classmethod
    def execute(self, query: str, params=None):
        if args.verbose:
            query_str = query
            if params != None:
                query_str = query.replace('%s', '{}').format(*params)
            logger.debug(f'DB execute "{query_str}"')

        with self.cursor() as cursor:
            try:
                cursor.execute(query, params)
            except (Exception, psycopg.Error) as error:
                logger.error(repr(error))
        self.connection().commit()

        return cursor

    @classmethod
    def execute_many(self, query: str, params_seq=[]):
        with self.cursor() as cursor:
            try:
                cursor.executemany(query, params_seq)
            except (Exception, psycopg.Error) as error:
                logger.error(repr(error))
        self.connection().commit()
        return cursor
