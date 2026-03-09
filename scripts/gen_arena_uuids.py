"""Generate deterministic UUIDs for arena zone, subzone, 121 rooms. One-off script."""

import uuid

NS = uuid.NAMESPACE_DNS
ZONE_UUID = uuid.uuid5(NS, "mythosmud.limbo/arena.zone")
SUBZONE_UUID = uuid.uuid5(NS, "mythosmud.limbo/arena.arena.subzone")
ROOMS = {}
for r in range(11):
    for c in range(11):
        ROOMS[(r, c)] = uuid.uuid5(NS, f"mythosmud.limbo_arena_arena_arena.{r}.{c}")

if __name__ == "__main__":
    print("ZONE", ZONE_UUID)
    print("SUBZONE", SUBZONE_UUID)
    for (r, c), uid in list(ROOMS.items())[:5]:
        print(f"ROOM_{r}_{c}", uid)
    print("...")
    print("ROOM_5_5", ROOMS[(5, 5)])
