import psycopg2
import logging
from config import get_config

def connect_to_postgres():
    """Connects to the PostgreSQL database using configuration parameters.

    Returns:
        psycopg2.connection: A database connection object.
    """

    try:
        params = get_config()
        logging.info(f"Connecting to PostgreSQL database with params: {params}")
        conn = psycopg2.connect(**params)
        logging.info("Connected to PostgreSQL database successfully.")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error connecting to PostgreSQL: {error}")
        raise

def execute_query(conn, query):
    """Executes a SQL query on the provided connection.

    Args:
        conn: A psycopg2 connection object.
        query: The SQL query to execute.

    Returns:
        list: A list of tuples representing the query results.
    """

    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"Error executing query: {error}")
        raise

if __name__ == "__main__":
    conn = connect_to_postgres()
    if conn:
        try:
            query = "SELECT version()"
            result = execute_query(conn, query)
            print(result)
        finally:
            conn.close()
            print("Database connection terminated.")
