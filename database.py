import sqlite3


con =sqlite3.connect("library.db")
cursor=con.cursor()

def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,quantity INTEGER NOT NULL,writer TEXT NOT NULL )")
    con.commit()


createtable()
def createmember():
    query="CREATE TABLE IF NOT EXISTS member(id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,status TEXT NOT NULL)"
    cursor.execute(query)
    con.commit()
def createbookmember():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookmemberrelation (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,memberid INTEGER NOT NULL,bookdid INTEGER NOT NULL)")
    con.commit()
createmember()
createbookmember()
con.close()