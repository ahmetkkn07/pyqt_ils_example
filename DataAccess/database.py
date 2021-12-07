
from DataAccess.config import config
import psycopg2
from Alogger import Alogger
logger = Alogger.Alogger(log_level=Alogger.LogLevel.ALL, log_to_file=False)


def get(query):
    data = None
    conn = None
    try:
        params = config()
        logger.info("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        raise Exception
    finally:
        if conn is not None:
            conn.close()
            logger.info("Database connection closed.")
    return data


def get_all(query):
    data = None
    conn = None
    try:
        params = config()
        logger.info("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        raise Exception
    finally:
        if conn is not None:
            conn.close()
            logger.info("Database connection closed.")
    return data


def add(query):
    try:
        params = config()
        logger.info("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        logger.error(error)
        raise Exception
    finally:
        if conn is not None:
            conn.close()
            logger.info("Database connection closed.")
