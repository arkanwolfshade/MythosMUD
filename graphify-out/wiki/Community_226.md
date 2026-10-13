# Community 226

> 68 nodes

## Key Concepts

- **ValueError** (136 connections)
- **GameConfig** (24 connections) — `server/config/models/game.py`
- **field_validator** (8 connections)
- **UUID** (6 connections)
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.validate_invite_code()** (4 connections) — `server/auth/endpoints.py`
- **.validate_password()** (4 connections) — `server/auth/endpoints.py`
- **.validate_combat_alert_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_performance_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_tick_interval()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_timeout()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_xp_multiplier()** (4 connections) — `server/config/models/game.py`
- **.validate_grace_period_seconds()** (4 connections) — `server/config/models/game.py`
- **.validate_max_connections()** (4 connections) — `server/config/models/game.py`
- **.validate_equip_requirements()** (4 connections) — `server/models/command_inventory.py`
- **.validate_pickup_requirements()** (4 connections) — `server/models/command_inventory.py`
- **.validate_unequip_requirements()** (4 connections) — `server/models/command_inventory.py`
- **.validate_use_requirements()** (4 connections) — `server/models/command_inventory.py`
- **.validate_spell_name()** (4 connections) — `server/models/command_magic.py`
- **.validate_spell_name()** (4 connections) — `server/models/command_magic.py`
- **.validate_spell_name()** (4 connections) — `server/models/command_magic.py`
- **.add_player_silently()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.npc_entered()** (4 connections) — `server/models/room.py`
- *... and 43 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (11 shared connections)
- [Community 237](Community_237.md) (8 shared connections)
- [Community 370](Community_370.md) (7 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (6 shared connections)
- [Community 326](Community_326.md) (5 shared connections)
- [Community 94](Community_94.md) (5 shared connections)
- [Container API Models](Container_API_Models.md) (5 shared connections)
- [Inventory Commands](Inventory_Commands.md) (4 shared connections)
- [Admin & Alias Commands](Admin_&_Alias_Commands.md) (4 shared connections)
- [Community 69](Community_69.md) (3 shared connections)
- [Community 537](Community_537.md) (3 shared connections)
- [Community 222](Community_222.md) (3 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/config/models/game.py`
- `server/models/command_inventory.py`
- `server/models/command_magic.py`
- `server/models/room.py`
- `server/tests/unit/config/test_config_models.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- `server/tests/unit/services/test_utility_threat.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 103 (43%)
- INFERRED: 139 (57%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*