import time

import db_handler as db

conn = None

def connect():
  global conn
  conn = db.connect("thanks.db") 

def new_thanks(from_id, to_id, message):
  global conn
  thanker = str(from_id)
  thankee = str(to_id)
  user_columns = ("user_id", "given", "received")
  thanks_columns = ("thanker_id", "recipient_id", "message", "timestamp")
  db.insert(conn, "thanks", thanks_columns, (thanker, thankee, message, time.time()))
  if len(db.select(conn, "users", "*", "WHERE user_id=" + thanker)) == 0:
    db.insert(conn, "users", user_columns, (thanker, 0, 0))
  if len(db.select(conn, "users", "*", "WHERE user_id=" + thankee)) == 0:
    db.insert(conn, "users", user_columns, (thankee, 0, 0))
  db.update(conn, "users", "given=given+1", "WHERE user_id=" + thanker)
  db.update(conn, "users", "received=received+1", "WHERE user_id=" + thankee)
