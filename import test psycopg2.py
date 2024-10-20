import psycopg2

def connect_to_postgres(host, dbname, user, password, port):
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
            port=port
        )
        print("Connected to PostgreSQL database successfully.")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to PostgreSQL: {error}")
        raise

def create_address_book_table(conn):
    """
    Creates a table named 'address_book' with columns for address and phone number.

    Args:
        conn: A psycopg2 connection object.
    """

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS address_book (
                id SERIAL PRIMARY KEY,
                address VARCHAR(255),
                SSN VARCHAR(11),
                AGE VARCHAR(2),
                phone_number VARCHAR(20)
            )
        """)
        conn.commit()
        print("Table 'address_book' created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error creating table: {error}")
        raise

if __name__ == "__main__":
    # Replace with your actual connection parameters
    host = "localhost"
    dbname = "cherry"
    user = "postgres"
    password = "1234"
    port = 5433

    conn = connect_to_postgres(host, dbname, user, password, port)
    if conn:
        try:
            create_address_book_table(conn)

            # Perform database operations here
            cursor = conn.cursor()
            # Example: Insert data into the table
            cursor.execute("INSERT INTO address_book (address, SSN, AGE, phone_number) VALUES  (%s, %s)", ("123 Main St","215-11-3237","50", "555-1234"))
            conn.commit()

            # Retrieve data from the table
            cursor.execute("SELECT * FROM address_book")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        finally:
            conn.close()
            print("Database connection terminated.")
