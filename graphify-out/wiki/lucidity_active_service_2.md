# lucidity active service

> 162 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_active_lucidity_service.py** (34 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **lucidity_recovery_commands.py** (25 connections) — `server/commands/lucidity_recovery_commands.py`
- **active_lucidity_service.py** (22 connections) — `server/services/active_lucidity_service.py`
- **handle_pray_command()** (21 connections) — `server/commands/lucidity_recovery_commands.py`
- **ActiveLucidityService** (20 connections) — `server/services/active_lucidity_service.py`
- **LucidityActionOnCooldownError** (16 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (15 connections) — `server/commands/lucidity_recovery_commands.py`
- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **handle_meditate_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **UnknownEncounterCategoryError** (10 connections) — `server/services/active_lucidity_service.py`
- **handle_group_solace_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (8 connections)
- **handle_therapy_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionError** (7 connections) — `server/services/active_lucidity_service.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_effect()** (6 connections) — `server/services/npc_combat_lucidity.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_restore_mp_for_action()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **UUID** (4 connections)
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- *... and 137 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (19 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (13 shared connections)
- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [command helpers functions](command_helpers_functions.md) (1 shared connections)
- [regeneration service magic](regeneration_service_magic.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 520 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*