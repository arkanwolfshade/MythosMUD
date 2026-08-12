# Room Service Tests

> 106 nodes

## Key Concepts

- **test_command_factories_utility.py** (51 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **.create_summon_command()** (14 connections) — `server/utils/command_factories_utility.py`
- **.create_cast_command()** (12 connections) — `server/utils/command_factories_utility.py`
- **.create_teleport_command()** (11 connections) — `server/utils/command_factories_utility.py`
- **.create_alias_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_unalias_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_learn_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_aliases_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **test_create_alias_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_aliases_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_unalias_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_unalias_command_multiple_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_invalid_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_negative_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_invalid_token()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_extra_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_too_many_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_invalid_direction()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_goto_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_spell_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_spells_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_learn_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- *... and 81 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (29 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (18 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (7 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (2 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Command Request App State](Command_Request_App_State.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 300 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*