import atexit
import sqlite3

def connect(db_name):
  db_path = "../storage/"+ db_name
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  atexit.register(c.close)
  return conn

def insert(conn, table, columns, args, autocommit=True):
  sql = "INSERT INTO " + table + totuple(columns) + " VALUES" + qmark_args(len(args))
  conn.cursor().execute(sql, args) 
  if autocommit:
    conn.commit()
  return conn.cursor().lastrowid

def update(conn, table, what, conditions, autocommit=True):
  sql = "UPDATE " + table + " SET " + what + " " + conditions
  conn.cursor().execute(sql)
  if autocommit:
    conn.commit()
  return conn.cursor().lastrowid

def select(conn, table, what, conditions):
  res = conn.cursor().execute("SELECT " + what + " FROM " + table + " " + conditions)
  return res.fetchall()

def qmark_args(num):
  s = '('
  for i in range(num - 1):
    s += '?,'
  return s + '?)'

def totuple(args):
  s = '('
  for arg in args:
    s += arg + ','
  return s[:len(s)-1] + ')'
