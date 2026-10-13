# Community 899

> 17 nodes

## Key Concepts

- **SpellCostsService** (16 connections) — `server/game/magic/spell_costs.py`
- **.apply_costs()** (7 connections) — `server/game/magic/spell_costs.py`
- **._notify_mp_update()** (7 connections) — `server/game/magic/spell_costs.py`
- **._spend_lucidity_if_required()** (6 connections) — `server/game/magic/spell_costs.py`
- **UUID** (6 connections)
- **._apply_corruption_if_mythos()** (5 connections) — `server/game/magic/spell_costs.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **Spell** (4 connections)
- **.__init__()** (3 connections) — `server/game/magic/spell_costs.py`
- **Any** (3 connections)
- **Apply spell costs (MP and lucidity if Mythos). Args: player_id: Player ID…** (1 connections) — `server/game/magic/spell_costs.py`
- **Restore magic points to a player. Args: player_id: Player ID amount: Amount of…** (1 connections) — `server/game/magic/spell_costs.py`
- **Service for applying spell costs. Handles MP, lucidity, and corruption costs…** (1 connections) — `server/game/magic/spell_costs.py`
- **Initialize the spell costs service. Args: player_service: Player service for…** (1 connections) — `server/game/magic/spell_costs.py`
- **Deduct lucidity cost in-place on stats, for Mythos spells that require it.** (1 connections) — `server/game/magic/spell_costs.py`
- **Apply corruption via CorruptionService for Mythos spells that carry a…** (1 connections) — `server/game/magic/spell_costs.py`
- **Send a player_update event so the client reflects the new MP (and current…** (1 connections) — `server/game/magic/spell_costs.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (2 shared connections)
- [Community 50](Community_50.md) (2 shared connections)
- [API Response Models](API_Response_Models.md) (2 shared connections)
- [Magic & Tick Services](Magic_&_Tick_Services.md) (1 shared connections)
- [Community 233](Community_233.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_costs.py`

## Audit Trail

- EXTRACTED: 36 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*