import sqlite3

# conn = sqlite3.connect(':memory:')  # If we want to temporarily store the database in memory

connection = sqlite3.connect('Customer.db')

c = connection.cursor()  # Create Cursor

# Create a Table
'''c.execute(""" CREATE TABLE customers(

	first_name text,
	last_name text,
	email text
	)""")'''

'''many_customers = [('kanak', 'chaudhari', 'kanakchaudhari12@gmail.com'),
 ('honda', 'tohru', 'oppaiharem69@gmail.com'),
  ('nya', 'chan', 'Bwahahaha@outlook.jp')]'''

# c.executemany(" INSERT INTO customers values(?,?,?)", many_customers)

# c.execute(""" INSERT INTO customers values('will', 'smith', 'will@gmail.com')""")

""" DATA-TYPES IN sqlite3 :-
 1. NULL
 2. INTEGER (WHOLE NUMBER)
 3. REAL	(FLOAT)
 4. TEXT	
 5. BLOB	(IT IS USED FOR IMAGES, AUDIO, VIDEO ETC)

 """


 # Query the DATA-BASE
# c.execute("SELECT * FROM customers WHERE last_name = 'chaudhari'")
# c.execute("UPDATE customers SET first_name = 'Tohru', last_name = 'Honda' WHERE rowid = 4")
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
# c.execute("SELECT rowid, * FROM customers")
# c.fetchone()
# c.fetchmany(3)
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'ch%' and first_name LIKE 'ka%'")
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")

items = c.fetchall()
for item in items:
	print(item)

# print("Command Executed Successfully...")
connection.commit()  # commit our command

 # Clsoe our connection

connection.close()