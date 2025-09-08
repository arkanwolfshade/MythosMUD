import sqlite3

# Check database structure
conn = sqlite3.connect("data/players/players.db")
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print(f"  {table[0]}")

# Check players table structure
cursor.execute("PRAGMA table_info(players)")
columns = cursor.fetchall()
print("\nPlayers table structure:")
for col in columns:
    print(f"  {col[1]} ({col[2]})")

# Check for Ithaqua account
cursor.execute("SELECT * FROM players WHERE name='Ithaqua'")
ithaqua = cursor.fetchone()
if ithaqua:
    print("\nIthaqua account found:")
    print(f"  Player ID: {ithaqua[0]}")
    print(f"  User ID: {ithaqua[1]}")
    print(f"  Name: {ithaqua[2]}")
    print(f"  Stats: {ithaqua[3]}")
else:
    print("\nIthaqua account not found")

conn.close()
