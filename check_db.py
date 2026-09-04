import sqlite3
conn = sqlite3.connect('drugguard.db')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]
print(f"Products in DB: {count}")
if count > 0:
    cursor.execute("SELECT product_id, product_name, genuine FROM products LIMIT 3")
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} (Genuine: {row[2]})")
conn.close()
