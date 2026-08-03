# event bus events

> 5 nodes

## Key Concepts

- **.__init__()** (8 connections) — `server/services/combat_monitoring_service.py`
- **Alert** (6 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_config()** (5 connections) — `server/services/combat_configuration_service.py`
- **Get the global combat configuration service instance.      Returns:         Comb** (1 connections) — `server/services/combat_configuration_service.py`
- **Initialize the combat monitoring service.** (1 connections) — `server/services/combat_monitoring_service.py`

## Relationships

- [combat monitoring service](combat_monitoring_service.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [npc combat service](npc_combat_service.md) (1 shared connections)
- [combat configuration service](combat_configuration_service.md) (1 shared connections)
- [main rationale failure()](main_rationale_failure%28%29.md) (1 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (1 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (1 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)
- [service feature services](service_feature_services.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/services/combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 18 (86%)
- INFERRED: 3 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*