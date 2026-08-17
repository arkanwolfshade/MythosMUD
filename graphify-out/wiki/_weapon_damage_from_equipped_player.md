# _weapon_damage_from_equipped_player

> 7 nodes

## Key Concepts

- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_attacker_stats_dict_from_full_player()** (3 connections) — `server/services/combat_turn_participant_actions.py`
- **PrototypeRegistry** (2 connections)
- **Normalize full_player.get_stats() to a dict for damage math.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve rolled damage and type from main-hand weapon, or unarmed fallback.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Return (player_service, registry, async_persistence) from app container, or…** (1 connections) — `server/services/combat_turn_participant_actions.py`

## Relationships

- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (6 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (2 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (1 shared connections)
- [models/combat.py](models-combat.py.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 16 (73%)
- INFERRED: 6 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*