# Services Lucidity Repository

> 89 nodes · cohesion 0.03

## Key Concepts

- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityExposureState** (23 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **LucidityRepository** (14 connections) — `server/services/lucidity_repository.py`
- **lucidity_repository.py** (11 connections) — `server/services/lucidity_repository.py`
- **UUID** (9 connections)
- **.delete_cooldowns_by_action_code_pattern()** (6 connections) — `server/services/lucidity_repository.py`
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **_utc_now()** (5 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (5 connections) — `server/services/lucidity_service.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **Base** (4 connections)
- **.__init__()** (4 connections) — `server/services/lucidity_service.py`
- **Any** (3 connections)
- **datetime** (3 connections)
- **datetime** (3 connections)
- **test_lucidity_adjustment_log_creation()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- *... and 64 more nodes in this community*

## Relationships

- [Player Death Service Tests](Player_Death_Service_Tests.md) (18 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (11 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (8 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (4 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (4 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (4 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (2 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (2 shared connections)
- [Metadata Npc](Metadata_Npc.md) (2 shared connections)
- [Player Related Models](Player_Related_Models.md) (2 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (1 shared connections)
- [Postgres Adapter Infrastructure](Postgres_Adapter_Infrastructure.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/tests/unit/models/test_lucidity_models.py`

## Audit Trail

- EXTRACTED: 280 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*