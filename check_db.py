import sqlite3

# Check local database
conn = sqlite3.connect("data/local/players/local_players.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in local database:", tables)

# Check if there are any invite codes
try:
    cursor.execute("SELECT * FROM invites LIMIT 5")
    invite_codes = cursor.fetchall()
    print("Invite codes:", invite_codes)
except Exception as e:
    print("No invites table:", e)

# Check players
cursor.execute("SELECT name FROM players LIMIT 5")
players = cursor.fetchall()
print("Players:", players)

conn.close()
