# pylint.py

> 17 nodes

## Key Concepts

- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **._subject_for_event()** (4 connections) — `server/events/nats_event_bridge.py`
- **Any** (3 connections)
- **.start()** (2 connections) — `server/events/nats_event_bridge.py`
- **.stop()** (2 connections) — `server/events/nats_event_bridge.py`
- **Subscribe to NATS domain events and start receiving.** (1 connections) — `server/events/nats_event_bridge.py`
- **Stop the bridge and unsubscribe from NATS.** (1 connections) — `server/events/nats_event_bridge.py`
- **Bridges domain events between local EventBus and NATS for distribution. When…** (1 connections) — `server/events/nats_event_bridge.py`
- **Initialize the NATS EventBus bridge. Args: event_bus: Local EventBus instance…** (1 connections) — `server/events/nats_event_bridge.py`
- **Build NATS subject for an event.** (1 connections) — `server/events/nats_event_bridge.py`
- **Publish event to NATS for distribution to other instances. Args: event: Domain…** (1 connections) — `server/events/nats_event_bridge.py`
- **Process a NATS message - deserialize and inject into local EventBus. Public for…** (1 connections) — `server/events/nats_event_bridge.py`
- **Handle message received from NATS - deserialize and inject into local EventBus.** (1 connections) — `server/events/nats_event_bridge.py`

## Relationships

- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [Persistence Layer Async Migration Plan](Persistence_Layer_Async_Migration_Plan.md) (5 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (2 shared connections)
- [Logging Best Practices](Logging_Best_Practices.md) (1 shared connections)
- [required](required.md) (1 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (1 shared connections)

## Source Files

- `server/events/nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 29 (83%)
- INFERRED: 6 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*