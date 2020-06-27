import sqlite3

def connect(db_name, *argv):
  db_path = "../storage/"+ db_name
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  for arg in argv:
    arg(c)
  conn.commit()
  c.close()
