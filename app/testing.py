import sqlite3 
from werkzeug.security import check_password_hash, generate_password_hash

con = sqlite3.connect("contrast.db", autocommit=False)
cur = con.cursor()

cur.execute("INSERT INTO people (first_name, last_name, mobile, email) VALUES ('Hassan', 'Azad', '07403369618', 'm.h.azad-14@outlook.com' )")

result = cur.execute("SELECT id FROM people WHERE first_name = 'Hassan' AND last_name = 'Azad'")
people_id = result.fetchone()[0]


hash = generate_password_hash('Saharimran89')

cur.execute("INSERT INTO users VALUES(?, ?, ?)", (people_id, 'batpadman', hash))

for row in cur.execute("SELECT people_id, username FROM users"):
    print(row)

con.close()