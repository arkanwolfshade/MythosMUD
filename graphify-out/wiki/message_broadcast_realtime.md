# message broadcast realtime

> 16 nodes

## Key Concepts

- **apply_communication_dampening()** (13 connections) — `server/services/lucidity_communication_dampening.py`
- **test_lucidity_communication_dampening.py** (11 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **lucidity_communication_dampening.py** (6 connections) — `server/services/lucidity_communication_dampening.py`
- **should_block_shout()** (4 connections) — `server/services/lucidity_communication_dampening.py`
- **test_should_block_shout_deranged()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_whisper_uneasy_adds_strained_tag()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_deranged_shout_blocked()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_outgoing_no_glyph_when_roll_high()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_outgoing_appends_glyph()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_incoming_strips_punctuation()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_deranged_incoming_scrambles_words()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **Any** (1 connections)
- **Communication dampening utilities for lucidity system.  Implements communication** (1 connections) — `server/services/lucidity_communication_dampening.py`
- **Apply communication dampening based on lucidity tiers.      Args:         messag** (1 connections) — `server/services/lucidity_communication_dampening.py`
- **Check if shout should be blocked based on tier.** (1 connections) — `server/services/lucidity_communication_dampening.py`
- **Unit tests for lucidity communication dampening.** (1 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`

## Relationships

- [circuit breaker realtime](circuit_breaker_realtime.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/services/test_lucidity_communication_dampening.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*