import sqlite3
from db_handler import create
 
def create_users(cursor):
  try:
    cursor.execute("""CREATE TABLE users
                  (user_id, given, received)""")
  except:
    pass

def create_thanks(cursor):
  try:
    cursor.execute("""CREATE TABLE thanks
                  (thanker_id, recipient_id, message, timestamp)""")
  except:
    pass

create("thanks.db", create_users, create_thanks)
