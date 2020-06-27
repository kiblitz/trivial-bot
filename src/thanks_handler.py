import time

import db_handler as db

cursor = None

def connect():
  global cursor
  cursor = db.connect("thanks.db") 

def new_thanks(thanker, thankee, message):
  global cursor
  db.insert(cursor, "thanks", (thanker, thankee, message, time.time()))
  if db.select(cursor, "thanks", "*", "WHERE user_id=" + thanker) == None:
    db.insert(cursor, "thanks", (thanker, 0, 0))
  if db.select(cursor, "thanks", "*", "WHERE user_id=" + thankee) == None:
    db.insert(cursor, "thanks", (thankee, 0, 0))
  db.update(cursor, "thanks", "given=given+1", "WHERE user_id=" + thanker)
  db.update(cursor, "thanks", "received=received+1", "WHERE user_id=" + thankee)
