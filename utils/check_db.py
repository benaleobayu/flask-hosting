import mysql.connector
import os

# Ambil nilai dari variabel lingkungan
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

# Buat koneksi
def connection_check():
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=username,
            password=password
        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record[0])

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # Tutup koneksi jika sudah selesai
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")