# command base models

> 16 nodes

## Key Concepts

- **CombatBundle** (19 connections) — `server/container/bundles/combat.py`
- **combat.py** (13 connections) — `server/container/bundles/combat.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._handle_nats_unavailable()** (3 connections) — `server/container/bundles/combat.py`
- **Combat bundle: player combat, death, respawn, combat service, catatonia, lucidit** (1 connections) — `server/container/bundles/combat.py`
- **Combat-related services.** (1 connections) — `server/container/bundles/combat.py`
- **Failover callback that relocates catatonic players to the sanitarium.** (1 connections) — `server/container/bundles/combat.py`
- **Initialize combat services.** (1 connections) — `server/container/bundles/combat.py`
- **Raise if prerequisites for NATS combat are missing.** (1 connections) — `server/container/bundles/combat.py`
- **Start NATS message handler if available. Logs and swallows errors.** (1 connections) — `server/container/bundles/combat.py`
- **Handle case when NATS is not connected. Raises in prod, sets combat_service to N** (1 connections) — `server/container/bundles/combat.py`
- **Initialize NATS-dependent combat service and start NATS message handler.** (1 connections) — `server/container/bundles/combat.py`

## Relationships

- [Error Conversion](Error_Conversion.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (3 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (3 shared connections)
- [alias command models](alias_command_models.md) (3 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`

## Audit Trail

- EXTRACTED: 62 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*