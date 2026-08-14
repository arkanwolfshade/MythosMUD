# combat_turn_participant_actions.py

> 23 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_apply_physical_strength_bonus()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_strength_modifier_from_attacker_stats()** (4 connections) — `server/services/combat_turn_participant_actions.py`
- **_attacker_stats_dict_from_full_player()** (3 connections) — `server/services/combat_turn_participant_actions.py`
- **test_apply_physical_strength_bonus_adds_for_physical_only()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_strength_modifier_from_attacker_stats_defaults()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **UUID** (2 connections)
- **NPC and player turn execution for combat auto-progression. Extracted from…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Parse strength from attacker stats dict; default 50 when missing or invalid.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Add CoC-style strength bonus for physical attacks (same formula as NPC combat…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Normalize full_player.get_stats() to a dict for damage math.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve rolled damage and type from main-hand weapon, or unarmed fallback.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve damage and damage_type for a player auto-attack from equipped main_hand…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve damage, process attack, log, and update last_action_tick.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Return (player_service, registry, async_persistence) from app container, or…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve target stats dict for damage calculation (player or default).** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Strength modifier defaults to 50; digit strings coerce for bonus math.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Physical damage adds strength bonus above 50; other damage types do not.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Relationships

- [CombatService](CombatService.md) (8 shared connections)
- [test_combat_turn_participant_actions.py](test_combat_turn_participant_actions.py.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (4 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (3 shared connections)
- [AppConfig](AppConfig.md) (3 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 85 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*