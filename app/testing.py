from flask import g
import sqlite3 
from werkzeug.security import check_password_hash, generate_password_hash

# Connect to database
def get_db():
    db = sqlite3.connect('contrast.db')
    
    db.row_factory = sqlite3.Row
    return db

# function to query database
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    result = cur.fetchall()
    cur.close()
    return (result[0] if result else None) if one else result

def main():

    con = get_db()

    con.execute("DELETE FROM testing WHERE name = ?", ["Hassan"])

    con.commit()

    result = query_db("SELECT name, size FROM testing WHERE name = ?", ["Hassan"])
    print(result)

    con.close()







    # rows = query_db("SELECT * FROM users WHERE username = ?", ["batpadman"])
     
    #  if len(rows) != 1 or not check_password_hash(rows["hash"], request.form.get("password")):
    #     return apology("invalid username and/or password", 403)
     
    # for user in rows:
    #     print(user['username'])

    #     return
    
    
main()









# con = sqlite3.connect("contrast.db", autocommit=False)
# # cur = con.cursor()

# # cur.execute("INSERT INTO people (first_name, last_name, mobile, email) VALUES ('Hassan', 'Azad', '07403369618', 'm.h.azad-14@outlook.com' )")

# result = cur.execute("SELECT id FROM people WHERE first_name = 'Hassan' AND last_name = 'Azad'")
# people_id = result.fetchone()[0]


# hash = generate_password_hash('Saharimran89')

# cur.execute("INSERT INTO users VALUES(?, ?, ?)", (people_id, 'batpadman', hash))

# for row in cur.execute("SELECT people_id, username FROM users"):
#     print(row)

# con.close()