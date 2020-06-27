import sqlite3
import db_handler
 
def create_users(cursor):
  try:
    cursor.execute("""CREATE TABLE users
                  (user_id INTEGER, given INTEGER, received INTEGER)""")
  except:
    pass

def create_thanks(cursor):
  try:
    cursor.execute("""CREATE TABLE thanks
                  (thanker_id INTEGER, recipient_id INTEGER, message TEXT, timestamp TEXT)""")
  except:
    pass

db_handler.connect("thanks.db", create_users, create_thanks)
