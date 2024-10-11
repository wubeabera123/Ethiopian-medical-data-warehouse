import psycopg2
from psycopg2 import sql

def create_database():
    # Step 1: Connect to the 'postgres' database to create the 'data_warehouse' database
    db_params = {
        'dbname': 'postgres',   # Connect to the 'postgres' database (default)
        'user': 'postgres',     # Your PostgreSQL username
        'password': '12345',   # Your PostgreSQL password
        'host': 'localhost',    # Your host (local or remote)
        'port': 5432            # Default PostgreSQL port
    }
    
    try:
        # Establish connection to the 'postgres' database
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True  # Enable autocommit to run CREATE DATABASE outside a transaction
        cur = conn.cursor()
        
        # Check if 'data_warehouse' database exists
        cur.execute("SELECT 1 FROM pg_database WHERE datname = 'data_warehouse'")
        exists = cur.fetchone()  # Fetch result
        
        if not exists:
            # If the database doesn't exist, create it
            cur.execute(sql.SQL("CREATE DATABASE data_warehouse"))
            print("Database 'data_warehouse' created.")
        else:
            print("Database 'data_warehouse' already exists.")
        
        # Close cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    create_database()
