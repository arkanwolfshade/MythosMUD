import sqlite3

# Check users table structure and Ithaqua credentials
conn = sqlite3.connect("data/players/players.db")
cursor = conn.cursor()

# Check users table structure
cursor.execute("PRAGMA table_info(users)")
columns = cursor.fetchall()
print("Users table structure:")
for col in columns:
    print(f"  {col[1]} ({col[2]})")

# Check for Ithaqua user record
cursor.execute("SELECT * FROM users WHERE username='Ithaqua'")
ithaqua_user = cursor.fetchone()
if ithaqua_user:
    print("\nIthaqua user record found:")
    for i, col in enumerate(columns):
        print(f"  {col[1]}: {ithaqua_user[i]}")
else:
    print("\nIthaqua user record not found")

# Check all users
cursor.execute("SELECT username, id FROM users LIMIT 10")
users = cursor.fetchall()
print("\nFirst 10 users:")
for user in users:
    print(f"  {user[0]} -> {user[1]}")

conn.close()
