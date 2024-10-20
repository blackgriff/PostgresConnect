import psycopg2
from configparser import ConfigParser

def get_config(filename="database2.ini", section="postgresql"):
    """
    Reads configuration details from a specified INI file and section.

    Args:
        filename (str, optional): Path to the configuration file. Defaults to "database2.ini".
        section (str, optional): Name of the section containing database settings. Defaults to "postgresql".

    Returns:
        dict: A dictionary containing the parsed configuration values from the specified section.
            Returns an empty dictionary if the section is not found.

    Raises:
        IOError: If there's an error reading the configuration file.
    """

    parser = ConfigParser()
    try:
        parser.read(filename)
    except FileNotFoundError:
        raise IOError(f"Configuration file not found: {filename}")

    if not parser.has_section(section):
        return {}

    config = dict(parser.items(section))
    print(f"config: {config}")
    return config

def connect_to_postgres():
    """
    Connects to the PostgreSQL database using configuration parameters from database2.ini.

    Returns:
        psycopg2.connection: A database connection object.
    """

    try:
        params = get_config()
        conn = psycopg2.connect(**params)
        print("Connected to PostgreSQL database successfully.")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to PostgreSQL: {error}")
        raise

if __name__ == "__main__":
    conn = connect_to_postgres()
    if conn:
        try:
            # Perform database operations here
            cursor = conn.cursor()
            cursor.execute("SELECT version()")
            version = cursor.fetchone()
            print("PostgreSQL version:", version)
        finally:
            conn.close()
            print("Database connection terminated.")
