import sqlite3

# Connect to the NPC database
conn = sqlite3.connect("data/local/npcs/local_npcs.db")
cursor = conn.cursor()

# Check the schema of npc_definitions table
cursor.execute("PRAGMA table_info(npc_definitions)")
columns = cursor.fetchall()

print("NPC Definitions table schema:")
for column in columns:
    print(f"  {column[1]} ({column[2]})")

# Check what data exists for Dr. Francis Morgan
cursor.execute("SELECT * FROM npc_definitions WHERE name = ?", ("Dr. Francis Morgan",))
result = cursor.fetchone()

if result:
    print(f"\nDr. Francis Morgan data: {result}")
else:
    print("\nDr. Francis Morgan not found")

conn.close()
