# server npc behavior engine behaviorengine

> 25 nodes

## Key Concepts

- **Any** (12 connections)
- **._try_evaluators()** (7 connections) — `server/npc/behavior_engine.py`
- **.evaluate_condition()** (6 connections) — `server/npc/behavior_engine.py`
- **.execute_applicable_rules()** (5 connections) — `server/npc/behavior_engine.py`
- **.get_applicable_rules()** (5 connections) — `server/npc/behavior_engine.py`
- **._evaluate_boolean_condition()** (4 connections) — `server/npc/behavior_engine.py`
- **._evaluate_equality()** (4 connections) — `server/npc/behavior_engine.py`
- **._evaluate_inequality()** (4 connections) — `server/npc/behavior_engine.py`
- **._evaluate_numeric_comparison()** (4 connections) — `server/npc/behavior_engine.py`
- **.execute_action()** (4 connections) — `server/npc/behavior_engine.py`
- **.add_rule()** (3 connections) — `server/npc/behavior_engine.py`
- **.get_rules()** (3 connections) — `server/npc/behavior_engine.py`
- **.register_action_handler()** (3 connections) — `server/npc/behavior_engine.py`
- **Get all behavior rules.** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate equality condition (==). Returns: bool if condition matches, None if…** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate inequality condition (!=). Returns: bool if condition matches, None if…** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate numeric comparison conditions (>=, <=, >, <). Args: condition:…** (1 connections) — `server/npc/behavior_engine.py`
- **Try multiple evaluator methods in sequence. Args: condition: Condition string…** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate boolean conditions and variable lookups. Args: condition: Condition…** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate a condition string against context. Args: condition: Condition string…** (1 connections) — `server/npc/behavior_engine.py`
- **Get rules that are applicable given the current context. Args: context: Current…** (1 connections) — `server/npc/behavior_engine.py`
- **Register an action handler for a specific action. Args: action_name: Name of…** (1 connections) — `server/npc/behavior_engine.py`
- **Execute a specific action. Args: action_name: Name of the action to execute…** (1 connections) — `server/npc/behavior_engine.py`
- **Execute all applicable rules based on context. Args: context: Current context…** (1 connections) — `server/npc/behavior_engine.py`
- **Add a behavior rule to the engine. Args: rule: Rule dictionary with name,…** (1 connections) — `server/npc/behavior_engine.py`

## Relationships

- [server npc behavior engine](server_npc_behavior_engine.md) (12 shared connections)

## Source Files

- `server/npc/behavior_engine.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*