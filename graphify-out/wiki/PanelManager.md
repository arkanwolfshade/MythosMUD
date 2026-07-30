# PanelManager

> 31 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_base.py** (20 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **._get_target_stats()** (4 connections) — `server/npc/combat_integration_base.py`
- **.calculate_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **UUID** (3 connections)
- **._get_npc_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_npc_attack_to_nats()** (3 connections) — `server/npc/combat_integration_base.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **ABC** (2 connections)
- **Protocol** (2 connections)
- **.handle_npc_attack_on_player()** (2 connections) — `server/npc/combat_integration_protocols.py`
- **Base segment of NPC combat integration (damage, effects, attack orchestration).** (1 connections) — `server/npc/combat_integration_base.py`
- **Base implementation: damage, combat effects, and NPC attack orchestration.** (1 connections) — `server/npc/combat_integration_base.py`
- **Calculate damage based on attacker and target stats.          Args:** (1 connections) — `server/npc/combat_integration_base.py`
- **Execute the direct NPC attack path (no full combat service available).** (1 connections) — `server/npc/combat_integration_base.py`
- **Get target stats from player or use defaults.** (1 connections) — `server/npc/combat_integration_base.py`
- **Subclasses provide NPC stat defaults for damage resolution.** (1 connections) — `server/npc/combat_integration_base.py`
- **Subclasses publish DP updates after direct NPC damage.** (1 connections) — `server/npc/combat_integration_base.py`
- **Subclasses publish NPCAttacked to the event bus.** (1 connections) — `server/npc/combat_integration_base.py`
- *... and 6 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (10 shared connections)
- [init](init.md) (10 shared connections)
- [get asyncpg server settings for](get_asyncpg_server_settings_for.md) (5 shared connections)
- [Any](Any.md) (3 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [real time](real_time.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [login grace period](login_grace_period.md) (2 shared connections)
- [process dead players()](process_dead_players%28%29.md) (1 shared connections)
- [default cors origins()](default_cors_origins%28%29.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 116 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*