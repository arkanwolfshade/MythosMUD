# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-20-extend-look-command/spec.md

## Technical Requirements

### Command Model Extensions

**File:** `server/models/command.py`

- Extend `LookCommand` model with:
  - `target_type: Literal["player", "npc", "item", "container", "direction"] | None` - Explicit target type specification
  - `look_in: bool = False` - Flag for container inspection mode
  - `instance_number: int | None = None` - Instance number for targeting specific items/containers when multiple exist

### Command Parser Updates

**File:** `server/utils/command_parser.py`

- Update `_create_look_command()` method to:
  - Parse explicit type syntax: `/look player <name>`, `/look item <name>`, `/look container <name>`
  - Parse container inspection: `/look in <container>` sets `look_in=True`
  - Parse instance targeting: Extract `-N` or ` N` suffix from target string (e.g., `backpack-2` or `backpack 2`)
  - Remove diagonal directions (`northeast`, `northwest`, `southeast`, `southwest`) from direction validation
  - Preserve existing behavior for implicit targeting

### Look Command Handler Implementation

**File:** `server/commands/exploration_commands.py`

**Target Resolution Logic:**
1. If `target_type` is explicitly set, use that type only
2. Otherwise, try in priority order: Players → NPCs → Items → Containers → Directions
3. Support instance targeting when multiple matches exist

**Player Look Implementation:**
- Get players in current room via `room.get_players()` and `persistence.get_player_by_id()`
- Match by name (case-insensitive, partial match)
- Support instance targeting for multiple players with same name
- Display format:
  ```
  [Player Name]
  [Visible Equipment: head, torso, legs, hands, feet, main_hand, off_hand]
  Position: [standing/sitting/etc.]
  Health: [descriptive label]
  Lucidity: [descriptive label]
  ```

**Health/Lucidity Label Functions:**
- `_get_health_label(stats: dict) -> str`:
  - "healthy" if health > 75%
  - "wounded" if health 25-75%
  - "critical" if health 1-24%
  - "mortally wounded" if health <= 0
- `_get_lucidity_label(stats: dict) -> str`:
  - "lucid" if lucidity > 75%
  - "disturbed" if lucidity 25-75%
  - "unstable" if lucidity 1-24%
  - "mad" if lucidity <= 0

**Visible Equipment Filter:**
- Include only external slots: `head`, `torso`, `legs`, `hands`, `feet`, `main_hand`, `off_hand`
- Exclude: `ring`, `amulet`, `belt`, `backpack` (internal/hidden slots)

**Item Look Implementation:**
- Search order: Room drops → Player inventory → Equipped items → Containers
- Use `room_manager.list_room_drops()` for room items
- Use `player.get_inventory()` and `player.get_equipped_items()` for player items
- Search containers via `persistence.get_containers_by_room_id()` and `persistence.get_containers_by_entity_id()`
- Match by `item_name` (case-insensitive, partial match)
- Support instance targeting: `_parse_instance_number(target: str) -> tuple[str, int | None]`
- Retrieve item prototype via `app.state.prototype_registry.get(prototype_id)`
- Display format:
  ```
  [Item Name]
  [Long Description from ItemPrototypeModel]
  ```

**Container Look Implementation:**
- Search containers in: Room containers (`persistence.get_containers_by_room_id()`) and wearable containers (`persistence.get_containers_by_entity_id()`)
- Match by container name/description from metadata (case-insensitive, partial match)
- Support instance targeting for multiple containers
- If `look_in=True` or target resolves to container, show contents
- Convert container data to `ContainerComponent` for access to items, capacity, lock state
- Display format:
  ```
  [Container Name/Description]

  Contents:
  [List of items with quantities]

  Capacity: [X/Y slots used]
  Lock Status: [unlocked/locked/sealed]
  ```

**Helper Functions:**
- `_get_players_in_room(room: Room, persistence: PersistenceLayer) -> list[Player]`
- `_get_health_label(stats: dict) -> str`
- `_get_lucidity_label(stats: dict) -> str`
- `_get_visible_equipment(player: Player) -> dict[str, dict]`
- `_find_item_in_room(room: Room, room_manager, target: str, instance_number: int | None) -> dict | None`
- `_find_item_in_inventory(player: Player, target: str, instance_number: int | None) -> dict | None`
- `_find_item_in_equipped(player: Player, target: str, instance_number: int | None) -> dict | None`
- `_find_item_in_containers(room: Room, player: Player, persistence: PersistenceLayer, target: str, instance_number: int | None) -> dict | None`
- `_find_container_in_room(room: Room, persistence: PersistenceLayer, target: str, instance_number: int | None) -> ContainerComponent | None`
- `_find_container_wearable(player: Player, persistence: PersistenceLayer, target: str, instance_number: int | None) -> ContainerComponent | None`
- `_parse_instance_number(target: str) -> tuple[str, int | None]` - Extracts instance number from `target-2` or `target 2` format

### Integration Points

**Item Prototype Registry:**
- Access via `app.state.prototype_registry` (from ApplicationContainer)
- Use `prototype_registry.get(prototype_id)` to retrieve `ItemPrototypeModel`
- Extract `long_description` field for item look display

**Container Service:**
- Use `persistence.get_containers_by_room_id(room_id)` for environmental containers
- Use `persistence.get_containers_by_entity_id(player_id)` for wearable containers
- Convert raw container data to `ContainerComponent` using `ContainerComponent.model_validate()`
- Access container properties: `items`, `capacity_slots`, `lock_state`, `metadata`

**Room Manager:**
- Use `room_manager.list_room_drops(room_id)` for room items
- Access via `app.state.connection_manager.room_manager`

### Error Handling

- Return appropriate error messages for:
  - Player not found: "You don't see anyone named '<target>' here."
  - Item not found: "You don't see any '<target>' here."
  - Container not found: "You don't see any '<target>' here."
  - Multiple matches: "You see multiple <type>s matching '<target>': [list]"
  - Instance out of range: "There aren't that many '<target>' here."

### Testing Requirements

**Unit Tests (`server/tests/unit/commands/test_exploration_commands.py`):**
- Test player look with various health/lucidity states
- Test item look in different locations (room, inventory, equipped, container)
- Test container look with different lock states
- Test instance targeting (`backpack-2`, `backpack 2`)
- Test explicit syntax (`/look player <name>`, `/look item <name>`, etc.)
- Test priority resolution when multiple targets could match
- Test diagonal direction removal
- Test error cases (not found, multiple matches, instance out of range)

**Integration Tests:**
- Test player look with real players in room
- Test item look across all locations with real items
- Test container look with real containers
- Test instance targeting with multiple items/containers of same name
- Test priority resolution in realistic scenarios

### Help Documentation Updates

**File:** `server/help/help_content.py`

Update help text with new examples:
- `look player Armitage` - Look at a player
- `look item lantern` - Look at an item
- `look container backpack` - Look at a container
- `look in backpack` - Look inside a container
- `look item backpack-2` - Look at second backpack (instance targeting)
- `look item backpack 2` - Alternative instance targeting syntax

## External Dependencies

No new external dependencies required. This feature uses existing:
- Item prototype registry (already in ApplicationContainer)
- Container persistence layer (already implemented)
- Room manager (already in ConnectionManager)
- Player persistence (already in PersistenceLayer)
