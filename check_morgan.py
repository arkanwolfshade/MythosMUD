import json
import sqlite3

# Connect to the NPC database
conn = sqlite3.connect("data/local/npcs/local_npcs.db")
cursor = conn.cursor()

# Check Dr. Francis Morgan's spawn rules
cursor.execute("SELECT spawn_rules FROM npc_definitions WHERE name = ?", ("Dr. Francis Morgan",))
result = cursor.fetchone()

if result:
    spawn_rules = result[0]
    print(f"Dr. Francis Morgan spawn_rules: {spawn_rules}")

    # Try to parse as JSON if it's not None
    if spawn_rules:
        try:
            parsed_rules = json.loads(spawn_rules)
            print(f"Parsed spawn rules: {parsed_rules}")
        except json.JSONDecodeError:
            print("Spawn rules is not valid JSON")
else:
    print("Dr. Francis Morgan not found in database")

# Also check what room we're supposed to be in
cursor.execute(
    "SELECT id FROM rooms WHERE zone = ? AND sub_zone = ? AND room_number = ?", ("earth", "arkhamcity", "sanitarium")
)
room_result = cursor.fetchone()
if room_result:
    print(f"Sanitarium room ID: {room_result[0]}")

conn.close()
