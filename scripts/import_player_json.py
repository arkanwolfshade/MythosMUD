import sqlite3
import json
import os

DB_PATH = os.path.join("data", "players.db")
PLAYER_JSON = os.path.join("data", "players", "player_3ff4b997-1bed-42b9-a96e-0892c9e25357.json")

with open(PLAYER_JSON, "r", encoding="utf-8") as f:
    player = json.load(f)

stats = player["stats"]

row = (
    player["id"],
    player["name"],
    stats["strength"],
    stats["dexterity"],
    stats["constitution"],
    stats["intelligence"],
    stats["wisdom"],
    stats["charisma"],
    stats["sanity"],
    stats["occult_knowledge"],
    stats["fear"],
    stats["corruption"],
    stats["cult_affiliation"],
    player["current_room_id"],
    player["created_at"],
    player["last_active"],
    player["experience_points"],
    player["level"]
)

conn = sqlite3.connect(DB_PATH)
with conn:
    conn.execute("""
        INSERT OR REPLACE INTO players (
            id, name, strength, dexterity, constitution, intelligence, wisdom, charisma,
            sanity, occult_knowledge, fear, corruption, cult_affiliation,
            current_room_id, created_at, last_active, experience_points, level
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, row)
    print(f"Imported player {player['name']} ({player['id']}) into {DB_PATH}")
