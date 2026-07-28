# Archive Planning E 2 E

> 11 nodes · cohesion 0.20

## Key Concepts

- **.publish()** (6 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **Any** (3 connections)
- **Check if connected to NATS and healthy.          Returns:             bool: True** (1 connections) — `server/infrastructure/nats_broker.py`
- **Publish message to NATS subject.          Args:             subject: NATS subjec** (1 connections) — `server/infrastructure/nats_broker.py`
- **Subscribe to NATS subject with message handler.          Args:             subje** (1 connections) — `server/infrastructure/nats_broker.py`
- **Send request and wait for reply (request-reply pattern).          Args:** (1 connections) — `server/infrastructure/nats_broker.py`
- **Configure TLS settings for NATS connection (mirrors NATSService._configure_tls).** (1 connections) — `server/infrastructure/nats_broker.py`

## Relationships

- [Message Broker Errors](Message_Broker_Errors.md) (6 shared connections)
- [E 2 E Results Scenario](E_2_E_Results_Scenario.md) (1 shared connections)
- [NATS Message Schemas](NATS_Message_Schemas.md) (1 shared connections)
- [Pydantic Code Review](Pydantic_Code_Review.md) (1 shared connections)
- [Infrastructure Postgres Sql](Infrastructure_Postgres_Sql.md) (1 shared connections)
- [Services Service Room](Services_Service_Room.md) (1 shared connections)

## Source Files

- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*