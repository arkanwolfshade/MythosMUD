# Lucidity Recovery Commands

> 134 nodes · cohesion 0.02

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_active_lucidity_service.py** (34 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **handle_pray_command()** (22 connections) — `server/commands/lucidity_recovery_commands.py`
- **ActiveLucidityService** (20 connections) — `server/services/active_lucidity_service.py`
- **LucidityActionOnCooldownError** (16 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (15 connections) — `server/commands/lucidity_recovery_commands.py`
- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **Any** (8 connections)
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **_restore_mp_for_action()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **UUID** (4 connections)
- **test_handle_group_solace_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_naive_datetime()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_cooldown_object()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_expiry()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **_format_recovery_success_message()** (3 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (3 connections)
- **test_handle_folk_tonic_command_delegates()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 109 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (34 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (18 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (3 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 392 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*