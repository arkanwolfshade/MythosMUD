# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-11-15-container-system/spec.md

## Changes

1. **containers table (SQLite + PostgreSQL)**
   - `container_instance_id TEXT PRIMARY KEY`
   - `source_type TEXT NOT NULL` (`environment`, `equipment`, `corpse`)
   - `owner_id TEXT NULL` (player/npc id or null for shared props)
   - `room_id TEXT NULL` (room identifier for environmental/corpse containers)
   - `entity_id TEXT NULL` (player/npc id when wearable)
   - `lock_state TEXT NOT NULL DEFAULT 'unlocked'`
   - `capacity_slots INTEGER NOT NULL`
   - `weight_limit INTEGER NULL`
   - `decay_at TEXT NULL`
   - `allowed_roles TEXT NULL` (JSON array string)
   - `items_json TEXT NOT NULL` (canonical serialized `InventoryStack` list)
   - `metadata_json TEXT NULL`

2. **inventory payload schema updates**
   - Add optional `inner_container` object with `capacity_slots`, `items`, and metadata to `InventoryItem` records stored inside player inventory rows.

3. **Room definition augmentations**
   - For JSON-defined room objects, add `container` block:
     ```json
     "container": {
       "enabled": true,
       "capacity_slots": 8,
       "lock_state": "locked",
       "key_item_id": "arkham_library_key"
     }
     ```
   - World loader migrates this block into the `containers` table on startup.

## Specifications

- **SQLite migration script**
  ```sql
  CREATE TABLE IF NOT EXISTS containers (
      container_instance_id TEXT PRIMARY KEY,
      source_type TEXT NOT NULL,
      owner_id TEXT,
      room_id TEXT,
      entity_id TEXT,
      lock_state TEXT NOT NULL DEFAULT 'unlocked',
      capacity_slots INTEGER NOT NULL,
      weight_limit INTEGER,
      decay_at TEXT,
      allowed_roles TEXT,
      items_json TEXT NOT NULL,
      metadata_json TEXT
  );
  CREATE INDEX IF NOT EXISTS idx_containers_room ON containers(room_id);
  CREATE INDEX IF NOT EXISTS idx_containers_entity ON containers(entity_id);
  ```

- **PostgreSQL migration (future)**
  ```sql
  CREATE TABLE containers (
      container_instance_id UUID PRIMARY KEY,
      source_type TEXT NOT NULL,
      owner_id UUID,
      room_id TEXT,
      entity_id UUID,
      lock_state TEXT NOT NULL DEFAULT 'unlocked',
      capacity_slots INT NOT NULL,
      weight_limit INT,
      decay_at TIMESTAMPTZ,
      allowed_roles JSONB,
      items JSONB NOT NULL,
      metadata JSONB
  );
  CREATE INDEX idx_containers_room ON containers(room_id);
  CREATE INDEX idx_containers_entity ON containers(entity_id);
  ```

- **JSON schema**
  - Update `PLAYER_INVENTORY_SCHEMA.$defs.itemStack` to include:
    ```json
    "inner_container": {
      "type": "object",
      "additionalProperties": false,
      "required": ["capacity_slots", "items"],
      "properties": {
        "capacity_slots": {"type": "integer", "minimum": 1, "maximum": 20},
        "items": {"type": "array", "items": {"$ref": "#/$defs/itemStack"}},
        "lock_state": {"type": "string"},
        "allowed_roles": {"type": "array", "items": {"type": "string"}}
      }
    }
    ```

## Rationale

- Centralizing containers enables corpse, environmental, and wearable storage to share lifecycle code while preserving transactional integrity.
- Indexes on `room_id` and `entity_id` speed lookups during room load and player login.
- JSONB fields (PostgreSQL) provide flexible metadata without new columns, while SQLite stores canonical JSON strings for compatibility.
- Schema validation ensures nested containers cannot exceed slot limits, protecting inventory invariants.
