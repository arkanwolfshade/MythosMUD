# .apply_combat_effects

> 19 nodes

## Key Concepts

- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_attribute_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_unexpected_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_validation_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._apply_mental_effects()** (3 connections) — `server/npc/combat_integration_base.py`
- **UUID** (2 connections)
- **Exception** (1 connections)
- **ValidationError** (1 connections)
- **Apply combat effects to a target (player or NPC). Args: target_id: ID of the…** (1 connections) — `server/npc/combat_integration_base.py`
- **Convert target_id to UUID, accepting either string or UUID input.** (1 connections) — `server/npc/combat_integration_base.py`
- **Apply combat effects to a player.** (1 connections) — `server/npc/combat_integration_base.py`
- **Apply mental/occult effects (lucidity loss and fear) based on damage type.** (1 connections) — `server/npc/combat_integration_base.py`
- **Handle AttributeError (critical programming error).** (1 connections) — `server/npc/combat_integration_base.py`
- **Handle ValidationError (expected validation error).** (1 connections) — `server/npc/combat_integration_base.py`
- **Handle unexpected errors.** (1 connections) — `server/npc/combat_integration_base.py`
- **Return True if the target player is currently in login grace period.** (1 connections) — `server/npc/combat_integration_base.py`

## Relationships

- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (10 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`

## Audit Trail

- EXTRACTED: 35 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*