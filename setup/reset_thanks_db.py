import sqlite3
import db_handler
 
def reset_users(cursor):
  try:
    cursor.execute("""DELETE FROM users""")
  except:
    pass

def reset_thanks(cursor):
  try:
    cursor.execute("""DELETE FROM thanks""")
  except:
    pass

db_handler.connect("thanks.db", reset_users, reset_thanks)
