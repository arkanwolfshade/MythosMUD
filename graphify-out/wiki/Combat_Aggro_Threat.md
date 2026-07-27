# Combat Aggro Threat

> 80 nodes · cohesion 0.05

## Key Concepts

- **combat_turn_participant_actions.py** (37 connections) — `server/services/combat_turn_participant_actions.py`
- **aggro_threat.py** (22 connections) — `server/services/aggro_threat.py`
- **CombatParticipant** (19 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatInstance** (13 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatService** (13 connections) — `server/services/combat_turn_participant_actions.py`
- **update_aggro()** (13 connections) — `server/services/aggro_threat.py`
- **add_damage_threat()** (12 connections) — `server/services/aggro_threat.py`
- **UUID** (11 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (10 connections) — `server/services/aggro_threat.py`
- **_weapon_damage_from_equipped_player()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatInstance** (9 connections) — `server/services/aggro_threat.py`
- **AsyncPersistenceLayer** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **AppConfig** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **PrototypeRegistry** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **UUID** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **get_or_create_hate_list()** (8 connections) — `server/services/aggro_threat.py`
- **process_npc_turn()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **PlayerService** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **apply_taunt()** (7 connections) — `server/services/aggro_threat.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **combat_service_end.py** (7 connections) — `server/services/combat_service_end.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- *... and 55 more nodes in this community*

## Relationships

- [[Combat Command Handler]] (13 shared connections)
- [[Combat Service Bundle]] (12 shared connections)
- [[Weapon Resolution Helpers]] (11 shared connections)
- [[Combat Taunt Tests]] (11 shared connections)
- [[Async Persistence Layer]] (9 shared connections)
- [[Application DI Bundles]] (9 shared connections)
- [[Combat Domain Events]] (9 shared connections)
- [[NPC Admin API]] (9 shared connections)
- [[Spell Effect Protocols]] (4 shared connections)
- [[Combat Attack Service]] (2 shared connections)
- [[Application Config Settings]] (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 367 (88%)
- INFERRED: 49 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
