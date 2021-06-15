import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="123",
        host="127.0.0.1",
        port=3306,
        database="deneme"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute(
    "SELECT search_engine,url FROM list",)
with open('wordlist.txt', 'a') as the_file:
    for (search_engine, url) in cur:
        print(f"Arama Moturu: {search_engine}, Url Adresi: {url}")
        the_file.write(f"{url}\n")


