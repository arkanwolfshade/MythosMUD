# populate_npc_sample_data.py

> 22 nodes

## Key Concepts

- **Any** (13 connections)
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (3 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (3 connections) — `server/caching/cache_service.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (3 connections) — `server/caching/cache_service.py`
- **Initialize the room cache service. Args: persistence: Persistence layer instance** (2 connections) — `server/caching/cache_service.py`
- **Get room data with caching. Args: room_id: The room ID Returns: Room data…** (1 connections) — `server/caching/cache_service.py`
- **Get room data with caching (synchronous version). Args: room_id: The room ID…** (1 connections) — `server/caching/cache_service.py`
- **Initialize the NPC cache service. Args: npc_service: NPC service instance** (1 connections) — `server/caching/cache_service.py`
- **Get NPC definitions with caching. Args: session: Database session Returns: List…** (1 connections) — `server/caching/cache_service.py`
- **Get a specific NPC definition with caching. Args: session: Database session…** (1 connections) — `server/caching/cache_service.py`
- **Get NPC spawn rules with caching. Args: session: Database session Returns: List…** (1 connections) — `server/caching/cache_service.py`
- **Initialize the profession cache service. Args: persistence: Persistence layer…** (1 connections) — `server/caching/cache_service.py`
- **Get all professions with caching. Returns: List of profession objects** (1 connections) — `server/caching/cache_service.py`
- **Get a specific profession by ID with caching. Args: profession_id: The…** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [.create_get_command](create_get_command.md) (8 shared connections)
- [test_event_publisher_helpers.py](test_event_publisher_helpers.py.md) (5 shared connections)
- [identify_critical_code.py](identify_critical_code.py.md) (4 shared connections)
- [main](main.md) (2 shared connections)
- [AGENTS.md](AGENTS.md.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*