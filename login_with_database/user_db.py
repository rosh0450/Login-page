import sqlite3
from tabulate import tabulate

def user_db():
    con=sqlite3.connect(database="employee2.db")
    cur=con.cursor()
    

    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, f_name text, l_name text, contact text, email text, question text, answer text, password text)")
    con.commit()

    #cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, charges text, description text)")
    #con.commit()
'''
    cur1=con.cursor()
    cur1.execute("select * from employee")

    print(tabulate(cur1, headers=["ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"], tablefmt="fancy_grid"))
'''
    con.close()

    

user_db()
