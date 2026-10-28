# PlayerCombatService

> 46 nodes · cohesion 0.09

## Key Concepts

- **test_combat_status_message_categories.py** (47 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **CombatMessagingIntegration** (23 connections) — `server/services/combat_messaging/integration.py`
- **asyncio** (13 connections)
- **test_phantom_combat_line_matches_real_npc_category_and_never_mints_its_own()** (10 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_first_awaited_args()** (8 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_npc_attacked_and_took_damage_are_combat_hit()** (8 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_sent_personal()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_sent_room()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_combat_attack_categories_follow_each_recipients_perspective()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_combat_state_notices_are_combat_status()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_player_attacked_is_combat_hurt()** (7 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_dispatched()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_published_data()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_combat_ended_is_combat_status()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_mortally_wounded_lines_are_combat_status_for_both_recipients()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_player_death_lines_are_combat_death_for_both_recipients()** (6 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_catatonia_is_status_lucidity()** (5 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_dp_decay_is_status_health()** (5 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_lucidity_change_is_status_lucidity()** (5 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_npc_death_line_is_combat_death()** (5 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **test_rescue_update_is_status_rescue()** (5 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_data()** (4 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **_participant()** (4 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **fixture** (4 connections)
- **combat_messaging/__init__.py** (3 connections) — `server/services/combat_messaging/__init__.py`
- *... and 21 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (21 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (20 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (7 shared connections)
- [test_inventory_display_helpers.py](test_inventory_display_helpers.py.md) (4 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [_handle_admin_hallucinate_command](_handle_admin_hallucinate_command.md) (2 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [ground_channel.py](ground_channel.py.md) (1 shared connections)
- [PerformanceTester](PerformanceTester.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/integration.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_status_message_categories.py`

## Audit Trail

- EXTRACTED: 128 (83%)
- INFERRED: 27 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*