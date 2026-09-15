# RoomCacheLoader

> 14 nodes

## Key Concepts

- **RoomCacheLoader** (26 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (8 connections) — `server/async_persistence_room_loader.py`
- **._build_room_data_from_row()** (7 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **._parse_zone_parts()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence_room_loader.py`
- **_row_optional_str()** (4 connections) — `server/async_persistence_room_loader.py`
- **_attributes_from_row()** (3 connections) — `server/async_persistence_room_loader.py`
- **._extract_exit_fields()** (3 connections) — `server/async_persistence_room_loader.py`
- **._log_exit_debug()** (3 connections) — `server/async_persistence_room_loader.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_loader.py`
- **._resolve_exit_room_ids()** (3 connections) — `server/async_persistence_room_loader.py`
- **Loads room data from the database and populates a room cache dict. Used by…** (1 connections) — `server/async_persistence_room_loader.py`

## Relationships

- [.load](load.md) (8 shared connections)
- [async_persistence_room_loader.py](async_persistence_room_loader.py.md) (7 shared connections)
- [ProcessedRoomData](ProcessedRoomData.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [_AsyncPersistenceRoomFacadeBase](_AsyncPersistenceRoomFacadeBase.md) (1 shared connections)
- [generate_room_id](generate_room_id.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 49 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*