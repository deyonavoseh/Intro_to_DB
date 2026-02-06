import mysql.connector

def create_database():
    """Create the alx_book_store database"""
    connection = None
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="DeBbydeyon13."  # Replace with YOUR actual MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            # Close cursor
            cursor.close()
            
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        # Close connection
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
