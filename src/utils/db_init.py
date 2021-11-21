from .db import DB
from .logger import logger

def init_db():
    query_create_events_data_hypertable = '''
        SELECT create_hypertable('events_data', 'time');
    '''

    with DB.cursor() as cursor:
        try:
            cursor.execute(query_create_events_data_hypertable)
        except Exception as error:
            logger.info(str(error))

    DB.connection().commit()
