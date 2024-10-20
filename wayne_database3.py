import psycopg2

def cherry_girl_postgres(host, dbname, user, password, port):
    """
    Connects to the PostgreSQL database using specified parameters.

    Args:
        host (str): The hostname of the PostgreSQL server.
        database (str): The name of the database to connect to.
        user (str): The username to use for authentication.
        password (str): The password for the user.
        port (int, optional): The port number of the PostgreSQL server. Defaults to 5432.

    Returns:
        psycopg2.connection: A database connection object.
    """

    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port,
        )
        print("Connected to Cherry Girl Love you successfully.")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to PostgreSQL: {error}")
        raise
        
if __name__ == "__main__":
    # Replace with your actual connection parameters
    host = "localhost"
    dbname = "cherry"
    user = "postgres"
    password = "1234"
    port = 5433

    conn = cherry_girl_postgres(host, dbname, user, password, port)
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
