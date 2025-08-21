import mysql.connector

def authonticate(user,passwd):
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host="localhost",       # Replace with your MySQL server host
        user="root",   # Replace with your MySQL username
        password="Gururaj@123", # Replace with your MySQL password
        database="mydatabase"  # Replace with your database name
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM Students")

    # Fetch and print the results
    for row in cursor.fetchall():
        if(row[1]==user and row[3]==passwd):
            return True
    else:
        return False
    

    # Close the connection
    cursor.close()
    connection.close()
print(authonticate('srujan','bca'))
