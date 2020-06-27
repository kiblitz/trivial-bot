import atexit
import sqlite3

def connect(db_name):
  db_path = "../storage/"+ db_name
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  atexit.register(c.close)
  return c

def insert(cursor, table, args, autocommit=True):
  sql = "INSERT INTO " + table + totuple(args) + " VALUES" + qmark_args(len(args))
  cursor.execute(sql, args) 
  if autocommit:
    cursor.commit()
  return cursor.lastrowid

def update(cursor, table, what, conditions, autocommit=True):
  sql = "UPDATE " + table + " SET " + what + " " + conditions
  cursor.execute(sql)
  if autocommit:
    cursor.commit()
  return cursor.lastrowid

def select(cursor, table, what, conditions):
  cursor.execute("SELECT " + what + " FROM " + table + " " + conditions)
  return cursor.fetchall()

def qmark_args(num):
  s = '('
  for i in range(num - 1):
    s += '?,'
  return s + '?)'

def totuple(args):
  s = '('
  for arg in args:
    s += arg + ','
  s = s[:len(s)-1] + ')'
