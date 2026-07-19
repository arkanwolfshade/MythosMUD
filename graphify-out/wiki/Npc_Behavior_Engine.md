# Npc Behavior Engine

> 25 nodes · cohesion 0.11

## Key Concepts

- **Any** (12 connections) — `server/npc/behavior_engine.py`
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
- **Evaluate equality condition (==).          Returns:             bool if conditio** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate inequality condition (!=).          Returns:             bool if condit** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate numeric comparison conditions (>=, <=, >, <).          Args:** (1 connections) — `server/npc/behavior_engine.py`
- **Try multiple evaluator methods in sequence.          Args:             condition** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate boolean conditions and variable lookups.          Args:             con** (1 connections) — `server/npc/behavior_engine.py`
- **Evaluate a condition string against context.          Args:             conditio** (1 connections) — `server/npc/behavior_engine.py`
- **Get rules that are applicable given the current context.          Args:** (1 connections) — `server/npc/behavior_engine.py`
- **Register an action handler for a specific action.          Args:             act** (1 connections) — `server/npc/behavior_engine.py`
- **Execute a specific action.          Args:             action_name: Name of the a** (1 connections) — `server/npc/behavior_engine.py`
- **Execute all applicable rules based on context.          Args:             contex** (1 connections) — `server/npc/behavior_engine.py`
- **Add a behavior rule to the engine.          Args:             rule: Rule diction** (1 connections) — `server/npc/behavior_engine.py`

## Relationships

- [[Npc Behavior Engine]] (12 shared connections)

## Source Files

- `server/npc/behavior_engine.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
