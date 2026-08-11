# Memory Threshold Monitor

> 25 nodes

## Key Concepts

- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **_perform_recovery_action()** (11 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_meditate_command()** (11 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (9 connections)
- **handle_therapy_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **_run_recovery_session()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_restore_mp_for_action()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **mp_regeneration_service()** (4 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **_format_recovery_success_message()** (3 connections) — `server/commands/lucidity_recovery_commands.py`
- **datetime** (2 connections)
- **Recovery rituals that steady a mind frayed by eldritch exposure.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Validate persistence and player for recovery action.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Format cooldown error message with remaining time.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Restore MP for meditation and pray actions, returning message if MP was restored** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Format success message for recovery action.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Common execution path for LCD recovery commands.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Invoke the meditation rite to anchor the mind.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Share solace among nearby allies to salve frayed nerves.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Undertake sanctioned therapy under Arkham Sanitarium protocols.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Swallow a dubious folk tonic brewed by cautiously reliable apothecaries.** (1 connections) — `server/commands/lucidity_recovery_commands.py`
- **Create an MPRegenerationService instance.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [Container Open Events](Container_Open_Events.md) (15 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (10 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (3 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (2 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (2 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (1 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)
- [Server Process Termination](Server_Process_Termination.md) (1 shared connections)
- [Cursor Agents Quick](Cursor_Agents_Quick.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 120 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*